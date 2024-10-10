from flask import Blueprint, jsonify, request, abort
from app.services.whisky_service import WhiskyService

whisky_routes = Blueprint('whisky_routes', __name__)


@whisky_routes.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({'status': 'success', 'message': 'pong!'})


@whisky_routes.route('/whiskies', methods=['GET', 'POST'])
def all_whiskies():
    """
    Get all whiskies or create a new whisky
    ---
    get:
      summary: Get all whiskies
      description: Returns a list of all whiskies.
      responses:
        200:
          description: List of whiskies
          content:
            application/json:
              schema: WhiskySchema(many=True)
    post:
      summary: Create a new whisky
      description: Creates a new whisky entry.
      requestBody:
        required: true
        content:
          application/json:
            schema: WhiskySchema
      responses:
        201:
          description: Whisky created
          content:
            application/json:
              schema: WhiskySchema
        400:
          description: Invalid input
    """
    if request.method == 'POST':
        whisky_data = request.get_json()
        if not whisky_data:
            abort(400, description="No input data provided")
        try:
            new_whisky = WhiskyService.create_whisky(whisky_data)
            return jsonify({'status': 'success', 'message': 'Whisky added!', 'whisky': new_whisky.to_dict()}), 201
        except Exception as e:
            abort(400, description=str(e))
    else:
        whiskies = WhiskyService.get_all_whiskies()
        return jsonify({'status': 'success', 'whiskies': [whisky.to_dict() for whisky in whiskies]})


@whisky_routes.route('/whiskies/<whisky_id>', methods=['GET', 'PUT', 'DELETE'])
def single_whisky(whisky_id):
    """
    Operations on a single whisky
    ---
    get:
      summary: Get a single whisky
      description: Returns a single whisky by ID.
      parameters:
        - in: path
          name: whisky_id
          required: true
          schema:
            type: string
      responses:
        200:
          description: A single whisky
          content:
            application/json:
              schema: WhiskySchema
        404:
          description: Whisky not found
    put:
      summary: Update a whisky
      description: Updates an existing whisky entry.
      parameters:
        - in: path
          name: whisky_id
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema: WhiskySchema
      responses:
        200:
          description: Whisky updated
          content:
            application/json:
              schema: WhiskySchema
        400:
          description: Invalid input
        404:
          description: Whisky not found
    delete:
      summary: Delete a whisky
      description: Deletes an existing whisky entry.
      parameters:
        - in: path
          name: whisky_id
          required: true
          schema:
            type: string
      responses:
        200:
          description: Whisky deleted
        404:
          description: Whisky not found
    """
    try:
        whisky = WhiskyService.get_whisky_by_id(whisky_id)
    except:
        abort(404, description="Whisky not found")

    if request.method == 'GET':
        return jsonify({'status': 'success', 'whisky': whisky.to_dict()})
    elif request.method == 'PUT':
        whisky_data = request.get_json()
        if not whisky_data:
            abort(400, description="No input data provided")
        try:
            updated_whisky = WhiskyService.update_whisky(whisky, whisky_data)
            return jsonify({'status': 'success', 'message': 'Whisky updated!', 'whisky': updated_whisky.to_dict()})
        except Exception as e:
            abort(400, description=str(e))
    elif request.method == 'DELETE':
        WhiskyService.delete_whisky(whisky)
        return jsonify({'status': 'success', 'message': 'Whisky deleted!'})
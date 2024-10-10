from flask import jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

class WhiskySchema(Schema):
   id = fields.Str(dump_only=True)
   name = fields.Str(required=True)
   distillery = fields.Str(required=True)
   age = fields.Int()
   region = fields.Str()
   tasted = fields.Bool()

spec = APISpec(
   title="Whisky API",
   version="1.0.0",
   openapi_version="3.0.2",
   plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

def setup_swagger(app):
   swagger_url = '/swagger'
   api_url = '/static/swagger/config.json'
   swaggerui_blueprint = get_swaggerui_blueprint(
       swagger_url,
       api_url,
       config={
           'app_name': "Whisky API"
       }
   )
   app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

   with app.test_request_context():
       # Register all routes
       for rule in app.url_map.iter_rules():
           if rule.endpoint != 'static':
               spec.path(view=app.view_functions[rule.endpoint])

   @app.route("/static/swagger/config.json")
   def create_swagger_spec():
       return jsonify(spec.to_dict())
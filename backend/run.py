from app import create_app, db
from app.models.whisky import Whisky

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Whisky': Whisky}

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
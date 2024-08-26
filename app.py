from flask import Flask
from views import best_mcc_bp, best_items_bp

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
        
    # Registrar blueprints
    app.register_blueprint(best_mcc_bp, url_prefix='/api')
    app.register_blueprint(best_items_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)

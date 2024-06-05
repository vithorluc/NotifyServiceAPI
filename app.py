from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .src.routes.health_routes import health_bp
from .config import make_celery


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notifications.db'
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

celery = make_celery(app)

app.register_blueprint(health_bp, url_prefix='/api')
# app.register_blueprint(user_bp, url_prefix='/api')
# app.register_blueprint(log_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)


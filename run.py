from flask import Flask
from database.database import db
from database.database import migrate

from enterprise_api.views.enterprise_views import app_enterprise

app = Flask(__name__)
app.config.from_object('enterprise_api.settings')

db.init_app(app)
migrate.init_app(app,db)

app.register_blueprint(app_enterprise)


app.run()
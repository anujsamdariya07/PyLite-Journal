from flask_blog import app, db
from flask_blog.models import User

with app.app_context():
  db.create_all()
from flask_blog import app, db
from flask_blog.models import User, Post

with app.app_context():
  posts = Post.query.paginate(per_page=2, page=6)
  # print(dir(posts))
  # print(posts.total)
  for post in posts.iter_pages():
    print(post, end=' ')

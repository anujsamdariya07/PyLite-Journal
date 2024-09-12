from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
  {
    'author': 'Anuj Samdariya',
    'title': 'JS Tutorial',
    'content': 'First Post Content',
    'date_posted': 'September 12, 2024',
  },
  {
    'author': 'John Doe',
    'title': 'TS Tutorial',
    'content': 'Second Post Content',
    'date_posted': 'September 14, 2024',
  },
]

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/home")
def home():
  return render_template('home.html', posts=posts, title='Home')

@app.route("/about")
def about():
  return render_template('about.html', title='About')

if __name__ == '__main__':
  app.run(debug=True)
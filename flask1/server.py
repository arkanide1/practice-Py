from flask import Flask , render_template , url_for
app = Flask(__name__)

@app.route('/<username>')
def hello_world(username=None):
    return render_template("index.html" , name=username)

@app.route('/blog.html')
def blog():
    return render_template("blog.html")


@app.route('/about.html')
def about():
    return render_template("about.html")

from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect("/thankyou.html")
    else:
        return "oops something went wrong"


def write_to_file(data):
    with open("data.txt", "a") as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        database.write(f"name:{name} , email:{email} , message:{message}\n")

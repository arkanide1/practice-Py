from flask import Flask, render_template, request, redirect
import csv
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
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "fif not save to database"
    else:
        return "oops something went wrong"


def write_to_file(data):
    with open("data.txt", "a") as database:
        email = data["email"]
        name = data["name"]
        message = data["message"]
        database.write(f"name:{name} , email:{email} , message:{message}\n")


def write_to_csv(data):
    with open("data.csv", newline='', mode="a") as database2:
        email = data["email"]
        name = data["name"]
        message = data["message"]

        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])
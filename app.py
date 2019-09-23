from flask import Flask, request
from flask import render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == "GET":
        return render_template("home_page.html", image="felix.jpg")
    else:
        request.url
        return render_template("home_page.html", xml="felix.jpg")


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name = "static/images/uploads/" + f.filename
        # Create the file
        open(file_name, "w")
        f.save(dst=file_name)
        return render_template("home_page.html", image=f.filename)


if __name__ == '__main__':
    app.run(debug=True)
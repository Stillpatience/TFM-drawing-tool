from flask import Flask, request
from flask import render_template
from PIL import Image
from xml_generator import generate_xml

app = Flask(__name__)
image = "mstile-150x150.png"
@app.route('/', methods=['GET', 'POST'])
def home_page():
    global image
    if request.files.get('file'):
        image = request.files.get('file').filename
    if request.method == "GET":
        return render_template("home_page.html", image=image)
    else:
        # Upload image
        if request.files.get('file'):
            f = request.files['file']
            file_name = "static/images/uploads/" + f.filename
            # Create the file
            open(file_name, "w")
            f.save(dst=file_name)
            print("here")
            return render_template("home_page.html", image=f.filename)
        # Generate XML
        else:
            x_offset = request.form.get("x")
            y_offset = request.form.get("y")
            print("Generating image for " + image)
            im = Image.open("static/images/uploads/" + image)
            width, height = im.size
            result = generate_xml(img_name=image, out_file="test3.xml", x_offset=int(x_offset)-width/2, y_offset=int(y_offset)-height/2)
            return render_template("home_page.html", image=image, xml=result)


if __name__ == '__main__':
    app.run(debug=True)

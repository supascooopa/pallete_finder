from flask import Flask, request, render_template, url_for, Response
from color_grabber import color_grabber
from excel_generator import color_excel_creator
from io import BytesIO

app = Flask("__app__")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        # requesting file
        pdf_file = request.files
        # streaming the file and reading it as bytes
        pdf_byte = pdf_file.get("file").stream.read()
        # changing the bytes into BytesIO to be able to feed it into read_pdf function
        io = BytesIO(pdf_byte)
        colors = color_grabber(image_file=io)
        return render_template("index.html", colors=colors)
    return render_template("index.html")


@app.route("/download")
def download():
    colors = request.args.getlist("color")
    colors_excel = color_excel_creator(colors)
    return Response(colors_excel,
                    mimetype="application/vnd.ms-excel",
                    headers={"Content-Disposition": "attachment;filename=your_colors.xlsx"})


if __name__ == "__main__":
    app.run(debug=True)
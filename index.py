from flask import Flask, redirect, render_template, request

app = Flask(__name__)


def payload_creator(product):
    start = True
    payload = ""
    for key, value in product.items():
        if int(value) != 0:
            if start:
                payload = key + "_" + value
                start = False
            else:
                payload = payload + "_" + key + "_" + value
        if start:
            payload = "error"
    return payload


def url_creator(product):
    payload = payload_creator(product)
    url = ""
    uri = "https://t.me/kamata_test_bot?start=o_x"
    if payload != "error":
        url = uri + payload
    else:
        url = "error"
    return url


@app.route("/")
def hello():

    # prints parent directory
    return render_template("advanced.html")


@app.route("/", methods=["POST"])
def process_form_data():
    product = request.form
    if url_creator(product) != "error":
        return redirect(url_creator(product), code=302)
    else:
        return "no item is selected", 400


if __name__ == "__main__":
    app.run(debug=True)

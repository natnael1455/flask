from flask import Flask, redirect, request, render_template

app = Flask(__name__)


def payload_creator(product):

    items = reduce(
        lambda x, key: x + "_" + key[0] + "_" + key[1] if int(key[1]) != 0 else x,
        product.items(),
        "",
    )

    return items[1:]


def url_creator(product):
    payload = payload_creator(product)

    uri = "http://t.me/natis_test_bot?start=o_x"

    if payload == "":
        url = "error"
    else:
        url = uri + payload
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

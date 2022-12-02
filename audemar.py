from flask import Flask, render_template, request, app

audemar = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

uzivatele = []



@audemar.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response


@audemar.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", users=uzivatele), 200


@audemar.route("/api/check-nickname/<nick>", methods=['GET', 'POST'])
def checkings(nick):
    if uzivatele.__contains__(nick):
        return "True"


@audemar.route('/registrace', methods=['GET', 'POST'])
def registrace():
    global uzivatele
    if request.method == "POST":
        nick = request.form["nick"]
        uzivatele.append(nick)
        print(uzivatele)

    return render_template("registrace.html"), 200


@audemar.route('/feedback', methods=['GET', 'POST'])
def feedback():
    return render_template("feedback.html"), 200


if __name__ == "__main__":
    audemar.run(host="0.0.0.0", port=8080)

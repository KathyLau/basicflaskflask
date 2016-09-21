from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return linkify("two") + linkify("/three")

@app.route("/two")
def foo():
    return linkify("three") + linkify("/")

@app.route("/three")
def fooo():
    return linkify("two") + linkify("/")

def linkify(url):
    return '<a href="' + url + '">' + url + '</a><br>'

if __name__=="__main__":
    app.run(debug=True)
    app.run()

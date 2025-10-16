from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/hello')
def api_hello():
    if "name" in request.args:
        return f"Hello, {request.args['name']}!"
    else:
        return "Hello, Ragazzi!"

if __name__ == "__main__":
    app.run()

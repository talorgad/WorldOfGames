from Utils import BAD_RETURN_CODE
from flask import Flask

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        file = open("Scores.txt", "r")
        score = file.read()
        html = """
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{}</div></h1>
            </body>
        </html>
        """.format(score)
        return html
    except:
        ERROR = BAD_RETURN_CODE
        html = """
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{ERROR}</div></h1>
            </body>
        </html>
        """
        return ERROR



if __name__ == "__main__":
    ip_address = '127.0.0.1'
    app.run(host=ip_address)

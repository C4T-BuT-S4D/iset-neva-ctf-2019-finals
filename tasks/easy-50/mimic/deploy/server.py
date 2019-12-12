from flask import Flask

app = Flask(__name__)

page = """
    <html>
        <head>
            <style>
                html,body,iframe {
                    width: 100%;
                    height: 100%;
                    margin: 0;
                }
            </style>
        </head>
        <body>
            <iframe src="https://www.youtube.com/embed/fIgm6lxvUfQ?autoplay=1&mute=1" allow="autoplay"></iframe>
        </body>
    </html>
"""

@app.route("/")
def index():
    return page

@app.route("/robots.txt")
def robots():
    return "flag{beep_"

@app.route("/humans.txt")
def humans():
    return "b3ep_be3p_b33p}"
    
if __name__ == "__main__":
    app.run(debug=False)
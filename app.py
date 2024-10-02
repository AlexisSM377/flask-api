from flask import Flask 
from routes import init_routes

app = Flask(__name__)

init_routes(app)


@app.route('/')
def home():
    return {
        "message" : "Bienvendo api flask Idgs 101"
    }


if __name__ == '__main__':
    app.run(debug=True)
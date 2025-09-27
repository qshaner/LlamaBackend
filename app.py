from flask import Flask
from flask_cors import CORS

from llamarama.myapp import simple_page

app = Flask(__name__)
CORS(app)
app.register_blueprint(simple_page)

if __name__ == "__main__":
    app.run(debug=True)

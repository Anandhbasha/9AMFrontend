from flask import Flask
from Router.Sturouter import studentBp

app = Flask(__name__)
app.register_blueprint(studentBp)

if __name__ == "__main__":
    app.run(debug=True)
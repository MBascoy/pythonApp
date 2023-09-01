from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud_example.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/', methods=['GET'])
def get_tasks():
    name = request.args.get("name")
    message = "hola"
    if name:
        message = "hola " + name
    return jsonify({'message': message})

@app.route('/<int:id>', methods=['GET'])
def get_task(id):

    return jsonify({'message': id})

@app.route('/', methods=['POST'])
def create_task():
    data = request.json
    title = data.get('title')
    return jsonify({'message': data.get('title')}), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
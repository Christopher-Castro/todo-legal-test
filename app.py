from os import name
from flask import Flask, request, jsonify, render_template
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__,
            static_folder='./frontend/dist/static',
            template_folder='./frontend/dist')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:example@db/flaskmysql'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(70), unique=True)
    name = db.Column(db.String(70))
    last_name = db.Column(db.String(70))
    phone_number = db.Column(db.String(70), unique=True)
    email = db.Column(db.String(70), unique=True)
    username = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(70))
    state = db.Column(db.Boolean, default=True)

    def __init__(self, uuid, name, last_name, phone_number, email, username, password, state):
        self.uuid = uuid
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password
        self.state = state


db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'uuid', 'name', 'last_name', 'phone_number', 'email', 'username', 'password', 'state')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/user', methods=['Post'])
def create_user():
    import uuid as uid
    uuid = uid.uuid1()
    name = request.json['name']
    last_name = request.json['last_name']
    phone_number = request.json['phone_number']
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    state = True


    new_user= User(uuid, name, last_name, phone_number, email, username, password, state)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


@app.route('/auth/login', methods=['POST'])
def get_user():
    
    password = request.json['password']

    user = User.query.filter_by(username=request.json['username']).first()
    
    if user is None: 
        return jsonify({'error_msg': 'User not exists'})
    elif user.password == password:
        return user_schema.jsonify(user)
    else:
        return jsonify({'error_msg': 'Wrong password'})


@app.route('/home', methods=['GET'])
def index():
    return jsonify('Welcome to my todo-legal Test, Christopher Castro.')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug=False)

from flask import Flask
# , request, redirect, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
# from secrets import API_SECRET_KEY

API_SECRET_KEY = 'abcdefg'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = API_SECRET_KEY

connect_db(app)
db.create_all()

"""Flask app for Cupcakes"""

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    """Route to get all cupcakes"""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]

    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes', methods=['POST'])
def make_cupcakes():
    """Adds a cupcake to databases"""

    data = request.json

    newCupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(newCupcake)
    db.session.commit()

    return (jsonify(newCupcake=cupcake.serialize()), 201)

@app.route('api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Returns a specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update specific cupcake"""

    data = request.json

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('api/cupcakes/<int: cupcake_id>', methods=['DELETE'])
def remove_cupcake(cupcake_id):
    """Delete a specific cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted") 

@app.route('/')
def cupcakeHTML():
    return render_template('cupcakes.html')
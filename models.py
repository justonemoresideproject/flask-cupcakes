from flask_sqlalchemy import SQLAlchemy

"""Models for Cupcake app."""

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__ = 'cupcakes'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor=db.Column(db.Text, nullable=False)
    size=db.Column(db.Text, nullable=False)
    rating=db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, default=DEFAULT_IMAGE_URL)

    def represent(self):
        return f'{self.id}, {self.flavor}, {self.size}, {self.rating}, {self.image}'

    def serialize(self):
        return { cupcake: {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image }
        }
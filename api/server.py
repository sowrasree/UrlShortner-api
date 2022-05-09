from api import app, db
# from core.models.users import User


from core.models import Model
from sqlalchemy import Column, String


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String)
    encrypted_password = Column(String)
    full_name = Column(String)
    mobile = Column(String)

    def __repr__(self):
        return '<User %r>' % self.id



@app.route("/")
def hello_world():

    users = User.query.all()
    return str([user.email for user in users])

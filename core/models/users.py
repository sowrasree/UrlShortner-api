import jwt
import hashlib
import datetime

from sqlalchemy import Column, String

from core import db
from core.libs import helpers, assertions
from core.models.principal import Principal
from core.config import Config


class User(db.Model):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    mobile = Column(String)

    created_at = Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, )
    updated_at = Column(db.TIMESTAMP(timezone=True), default=helpers.get_utc_now, onupdate=helpers.get_utc_now)

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def hash_password(password):
        obfuscated = '%s_%s' % (password, Config.HASH_SECRET)
        phash = hashlib.sha256(obfuscated.encode()).hexdigest()
        return phash

    @classmethod
    def upsert(cls, new_user: 'User'):
        user = new_user
        user.id = 'us_%s' % (helpers.generate_random_string())
        user.password = cls.hash_password(user.password)
        db.session.add(new_user)

        db.session.flush()
        return user

    @classmethod
    def filter(cls, *criterion):
        db_query = db.session.query(cls)
        return db_query.filter(*criterion)

    @classmethod
    def get_by_id(cls, _id):
        return cls.filter(cls.id == _id).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.filter(cls.email == email).first()

    def is_password_correct(self, password):
        return self.password == self.hash_password(password)

    def generate_refresh_token(self):
        payload = dict(
            user_id=self.id,
            exp=helpers.get_utc_now() + datetime.timedelta(days=7)
        )

        refresh_token = jwt.encode(
            payload,
            Config.JWT_REFRESH_SECRET,
            algorithm="HS256"
        )

        return refresh_token

    def generate_access_token(self):
        payload = dict(
            principal=Principal(
                user_id=self.id,
                scope=['ALL']
            ).to_dict(),
            exp=helpers.get_utc_now() + datetime.timedelta(hours=1)
        )

        access_token = jwt.encode(
            payload,
            Config.JWT_ACCESS_SECRET,
            algorithm="HS256"
        )

        return access_token

    @classmethod
    def validate_refresh_token(cls, refresh_token):
        is_jwt_valid = True

        try:
            payload = jwt.decode(refresh_token, Config.JWT_REFRESH_SECRET, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            is_jwt_valid = False

        assertions.assert_auth(is_jwt_valid is True, 'Invalid refresh_token found')
        user_id = payload['user_id']

        user: User = User.get_by_id(user_id)

        return user

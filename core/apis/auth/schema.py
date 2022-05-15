from marshmallow import Schema, EXCLUDE, fields, post_load, validate

from core.libs.helpers import GeneralObject
from core.models.users import User


class UserRegisterSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Email(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False, validate=validate.Regexp(r'[A-Za-z0-9@#$%^&+=]{8,}'))
    full_name = fields.String(required=True, allow_none=False)
    mobile = fields.String(required=True, allow_none=True)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return User(**data_dict)


class UserSigninSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    email = fields.Email(required=True, allow_none=False)
    password = fields.String(required=True, allow_none=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)


class UserSigninResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    refresh_token = fields.String(required=True, allow_none=False)


class AccessTokenIncomingSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    refresh_token = fields.String(required=True, allow_none=False)

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return GeneralObject(**data_dict)


class AccessTokenResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    access_token = fields.String(required=True, allow_none=False)


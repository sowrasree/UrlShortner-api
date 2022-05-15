from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.users import User

from .schema import (
    UserRegisterSchema, UserSigninSchema,
    UserSigninResponseSchema, AccessTokenIncomingSchema,
    AccessTokenResponseSchema
)

from ...libs import assertions

common_auth_resources = Blueprint('common_auth_resources', __name__)


@common_auth_resources.route('/signup', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
def register(incoming_payload):
    """Create or Edit an assignment"""
    user = UserRegisterSchema().load(incoming_payload)
    User.upsert(user)
    db.session.commit()

    return APIResponse.respond(data={})


@common_auth_resources.route('/signin', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
def signin(incoming_payload):
    """Create or Edit an assignment"""

    incoming_signin_object = UserSigninSchema().load(incoming_payload)

    user = User.get_by_email(
        email=incoming_signin_object.email
    )

    assertions.assert_auth(user is not None, "Invalid user/password")

    is_password_correct = user.is_password_correct(
        password=incoming_signin_object.password
    )

    assertions.assert_auth(is_password_correct is True, "Invalid user/password")

    #  generate refresh_token
    refresh_token = user.generate_refresh_token()

    user_signin_response = UserSigninResponseSchema().dump({'refresh_token': refresh_token})

    db.session.commit()
    return APIResponse.respond(data=user_signin_response)


@common_auth_resources.route('/access_token', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
def gen_access_token(incoming_payload):
    """Create or Edit an assignment"""

    incoming_signin_object = AccessTokenIncomingSchema().load(incoming_payload)
    refresh_token = incoming_signin_object.refresh_token

    user = User.validate_refresh_token(refresh_token)
    access_token = user.generate_access_token()

    user_access_token_response = AccessTokenResponseSchema().dump({'access_token': access_token})

    db.session.commit()
    return APIResponse.respond(data=user_access_token_response)

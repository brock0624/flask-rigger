# -*- coding: utf-8 -*-
from flask_restplus import Resource, fields, marshal_with, reqparse
from email_validator import validate_email as valid_email
from app.models import User
from app.utils.code import custom_abord, generate_response, ResponseCode

abort = custom_abord


def email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if valid_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))


# parse = reqparse.RequestParser()

# parse.add_argument(
#     'username', dest='username',
#     location='form', required=True,
#     help='The user\'s username',
# )
# parse.add_argument(
#     'email',
#     dest='email',
#     type=email,
#     location='form',
#     required=True,
#     help='The user\'s email',
# )

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'last_login_at': fields.String,
    'current_login_at': fields.String,
    'last_login_ip': fields.String,
    'current_login_ip': fields.String,
    'login_count': fields.Integer(default=0),
    'active': fields.Boolean,
    'confirmed_at': fields.String,
    'roles': fields.List(fields.Nested({
        'id': fields.Integer,
        'name': fields.String
    }))
}


class UsersView(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        # args = parse.parse_args()
        user = User.query.filter_by(id=id).first()
        return user

    @marshal_with(user_fields)
    def post(self):
        # args = parse.parse_args()
        user = User.query.filter_by(id=id).first()
        return user


class UsersList(Resource):
    # @marshal_with(user_fields)
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument("id", type=int, help="be  int", required=True)
        id = parse.parse_args().get("id")
        userslist = User.query.filter_by(id=id).all()
        if len(userslist) == 0:
            custom_abord(ResponseCode.CODE_NO_PARAM)
        else:
            userlist = []
            for userl in userslist:
                username = userl.username
                userlist.append(username)
            return generate_response(data=userlist, code=ResponseCode.code_success)

# -*- coding: utf-8 -*- 
from flask_restful import Resource, fields, marshal_with, reqparse, abort
from email_validator import validate_email as valid_email
from app.models import Codes
from app.code import custom_abord, generate_response, ResponseCode
from app.utils.common import query_to_dict


class StageCode(Resource):
    def get(self):
        codes = Codes.query.filter().all()
        codedict = query_to_dict(codes)
        code_dict = {}
        for code in codedict:
            code_dict[code.get('code')] = code.get('name')
        return code_dict

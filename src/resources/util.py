import json

from flask import Response
from flask.views import MethodView

from src.errors.errors import BaseAppException, GenericException


class BaseAppView(MethodView):
    @staticmethod
    def return_response_with_status_code(payload={}, status_code=502):
        return Response(json.dumps(payload), status=status_code)

    @staticmethod
    def return_error_response_with_status_code(base_exception, status_code=500):
        # in case of any generic exception which is not mentioned in errors.py
        if not isinstance(base_exception, BaseAppException):
            base_exception = GenericException(msg=str(base_exception))

        payload = {"errors": [{"code": base_exception.code, "code_str": base_exception.code_str,
                               "display_msg": base_exception.display_msg, "type": base_exception.err_type,
                               "msg": base_exception.msg}]}
        print(f"Error response : {payload}")
        return Response(json.dumps(payload), status=status_code, mimetype="application/json")

    @staticmethod
    def return_success_response_with_status_code(response, status_code=200):
        print(f"Success response : {response}")
        return Response(json.dumps(response), status=status_code, mimetype="application/json")
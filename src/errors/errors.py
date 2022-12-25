from src.errors.constants import ErrorCode, DisplayMsg, ErrorType


class BaseAppException(Exception):
    code = None
    code_str = None
    display_msg = None
    err_type = None
    msg = None

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        self.code = code
        self.code_str = str(code)
        self.display_msg = display_msg
        self.err_type = err_type
        self.msg = msg


class GenericException(BaseAppException):
    code = ErrorCode.GENERIC
    display_msg = DisplayMsg.OOPS_ERROR_OCCURRED
    err_type = ErrorType.GENERIC_ERROR
    msg = "Exception occurred while processing"

    def __init__(self, code=code, display_msg=display_msg, err_type=err_type, msg=msg):
        super(GenericException, self).__init__(code, display_msg, err_type, msg)
class ErrorCode(object):
    MISSING_INPUT_PARAMS = 1000
    SQL = 1001
    GENERIC = 1002
    AUTHENTICATION = 1003
    IDEMPOTENT = 1004
    THIRD_PARTY = 1005
    AUTHORISATION = 1006


class ErrorType(object):
    GENERIC_ERROR = "Generic"
    SQL = "Sql"
    AEROSPIKE = "Aerospike"
    JSON = "Json"
    THIRD_PARTY_API = "ThirdPartyAPI"
    AUTHENTICATION = "Authentication"
    MISSING_INPUT_PARAMS = "MissingInputParams"
    IDEMPOTENT = "Idempotent"
    BAD_REQUEST = "BadRequest"
    AUTHORISATION = "Authorisation"


class DisplayMsg(object):
    OOPS_ERROR_OCCURRED = "Oops! An Error occurred while processing your request!"
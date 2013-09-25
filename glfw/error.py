from glfw.constants import ErrorCode


class PriorErrorError(Exception):
    """ An error occured a while ago but nobody bothered to check
    """
    pass


class UnknownError(Exception):
    pass


class NotInitialised(Exception):
    pass


class NoCurrentContext(Exception):
    pass


class InvalidEnum(Exception):
    pass


class InvalidValue(Exception):
    pass


class OutOfMemory(Exception):
    pass


class APIUnavailable(Exception):
    pass


class VersionUnavailable(Exception):
    pass


class PlatformError(Exception):
    pass


class FormatUnavailable(Exception):
    pass


error_code_map = {
    ErrorCode.NOT_INITIALIZED: NotInitialised,
    ErrorCode.NO_CURRENT_CONTEXT: NoCurrentContext,
    ErrorCode.INVALID_ENUM: InvalidEnum,
    ErrorCode.INVALID_VALUE: InvalidValue,
    ErrorCode.OUT_OF_MEMORY: OutOfMemory,
    ErrorCode.API_UNAVAILABLE: APIUnavailable,
    ErrorCode.VERSION_UNAVAILABLE: VersionUnavailable,
    ErrorCode.PLATFORM_ERROR: PlatformError,
    ErrorCode.FORMAT_UNAVAILABLE: FormatUnavailable,
}

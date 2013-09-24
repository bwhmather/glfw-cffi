from glfw.constants import ErrorCode
from glfw._glfw import ffi, libglfw


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


_current_error = None

_error_types = {
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


def _on_error(error, description):
    global _current_error
    if not _current_error:
        _current_error = _error_types[error](description)

libglfw.glfwSetErrorCallback(ffi.callback('GLFWerrorfun', _on_error))


def check_error():
    global _current_error

    error, _current_error = _current_error, None
    if error:
        raise error

from glfw.constants import ErrorCode
from glfw._glfw import ffi, libglfw

import functools


class PriorErrorError(Exception):
    """ An error occured a while ago but nobody bothered to check
    """
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


def throw_errors(f):
    """ Decorate a function calling a glfw native function so that glfw errors
    are raised as exceptions.
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        global _current_error
        assert not _current_error

        error = None

        try:
            r = f(*args, **kwargs)
        finally:
            # always clear the error if the function raised something
            error, _current_error = _current_error, None

        if error:
            raise error

        return r
    return wrapper

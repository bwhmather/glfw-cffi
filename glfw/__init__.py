from glfw._glfw import ffi, libglfw
from glfw.error import throw_errors
from glfw.window import Window
import atexit


__all__ = ['Window', 'poll_events', 'wait_events']


if not libglfw.glfwInit():
    raise Exception()

atexit.register(libglfw.glfwTerminate)


#void glfwGetVersion(int* major, int* minor, int* rev);
# const char* glfwGetVersionString(void);
@throw_errors
def get_version(verbose=False):
    if not verbose:
        major = ffi.new('int *')
        minor = ffi.new('int *')
        rev = ffi.new('int *')

        libglfw.glfwGetVersion(major, minor, rev)

        return '{}.{}.{}'.format(major, minor, rev)
    else:
        return str(libglfw.glfwGetVersionString())


#GLFWerrorfun glfwSetErrorCallback(GLFWerrorfun cbfun);
# TODO
#void glfwPollEvents(void);
@throw_errors
def poll_events():
    """ Process events that have already been received and return immediately.

    This will invoke all relevant window callbacks in the current thread.

    This function is not required for joystick input to work.

    .. note::
      - This function may only be called from the main thread.
      - This function may not be called from a callback.
      - On some platforms, certain callbacks may be called outside of a call
        to one of the event processing functions.

    .. seealso::
      :py:fun:`wait_events`

    """
    libglfw.glfwPollEvents()


#void glfwWaitEvents(void);
@throw_errors
def wait_events():
    """ Sleep until at least one event has been received.

    This will invoke all relevant window callbacks in the current thread.

    This function is not required for joystick input to work.

    .. note::
      - This function may only be called from the main thread.
      - This function may not be called from a callback.
      - On some platforms, certain callbacks may be called outside of a call
        to one of the event processing functions.

    .. seealso::
        :py:fun:`poll_events`

    """
    libglfw.glfwWaitEvents()

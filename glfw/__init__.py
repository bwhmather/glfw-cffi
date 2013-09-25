from glfw._glfw import ffi, call
from glfw.window import Window


__all__ = ['Window', 'poll_events', 'wait_events']

#void glfwGetVersion(int* major, int* minor, int* rev);
# const char* glfwGetVersionString(void);
def get_version(verbose=False):
    if not verbose:
        major = ffi.new('int *')
        minor = ffi.new('int *')
        rev = ffi.new('int *')

        call('glfwGetVersion', major, minor, rev)

        return '{}.{}.{}'.format(major, minor, rev)
    else:
        return str(call('glfwGetVersionString'))


#GLFWerrorfun glfwSetErrorCallback(GLFWerrorfun cbfun);
# TODO
#void glfwPollEvents(void);
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
    call('glfwPollEvents')


#void glfwWaitEvents(void);
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
    call('glfwWaitEvents')

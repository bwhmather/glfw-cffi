from glfw._glfw import ffi, libglfw
from glfw.window import Window
import atexit


__all__ = ['Window', 'poll_events', 'wait_events']


if not libglfw.glfwInit():
    raise Exception()

atexit.register(libglfw.glfwTerminate)


#void glfwGetVersion(int* major, int* minor, int* rev);
# const char* glfwGetVersionString(void);
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
def poll_events():
    libglfw.glfwPollEvents()

#void glfwWaitEvents(void);
def wait_events():
    libglfw.glfwWaitEvents()


#void glfwSetClipboardString(GLFWwindow* window, const char* string);
#const char* glfwGetClipboardString(GLFWwindow* window);
#double glfwGetTime(void);
#void glfwSetTime(double time);
#void glfwSwapInterval(int interval);
#int glfwExtensionSupported(const char* extension);
#GLFWglproc glfwGetProcAddress(const char* procname);

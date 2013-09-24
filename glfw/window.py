from glfw._glfw import ffi, libglfw
from glfw.error import throw_errors
from glfw.monitor import Monitor

__all__ = ['Window']

class Window(object):
    #GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
    @throw_errors
    def __init__(self, width, height, title, monitor=None):
        self._title = str(title)
        if not isinstance(title, ffi.CData):
            title = ffi.new('const char[]', title.encode('utf-8'))

        if isinstance(monitor, Monitor):
            monitor = monitor._monitor

        if monitor is None:
            monitor = ffi.NULL


        self._window = libglfw.glfwCreateWindow(width, height, title, monitor, ffi.NULL);

    #void glfwMakeContextCurrent(GLFWwindow* window);
    @throw_errors
    def make_current(self):
        libglfw.glfwMakeContextCurrent(self._window)

    #void glfwSwapBuffers(GLFWwindow* window);
    @throw_errors
    def swap_buffers(self):
        libglfw.glfwSwapBuffers(self._window);


    #void glfwDefaultWindowHints(void);
    #void glfwWindowHint(int target, int hint);
    #GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);


    # TODO
    #void glfwDestroyWindow(GLFWwindow* window);
    #int glfwWindowShouldClose(GLFWwindow* window);
    @throw_errors
    def should_close(self):
        return bool(libglfw.glfwWindowShouldClose(self._window))

    #void glfwSetWindowShouldClose(GLFWwindow* window, int value);
    @throw_errors
    def close(self):
        raise NotImplementedError()

    #void glfwSetWindowTitle(GLFWwindow* window, const char* title);
    @throw_errors
    def get_title(self):
        return self._title

    @throw_errors
    def set_title(self, title):
        self._title = str(title)
        if not isinstance(title, ffi.CData):
            title = ffi.new('const char *', title)
        libglfw.glfwSetWindowTitle(self._window, title)

    title = property(fget=get_title, fset=set_title)

    #void glfwGetWindowPos(GLFWwindow* window, int* xpos, int* ypos);
    @throw_errors
    def get_position(self):
        x = ffi.new('int *')
        y = ffi.new('int *')

        libglfw.glfwGetWindowPos(self._window, x, y)

        return int(x), int(y)

    #void glfwSetWindowPos(GLFWwindow* window, int xpos, int ypos);
    @throw_errors
    def set_position(self, x, y):
        libglfw.glfwSetWindowSize(self._window, x, y)

    position = property(fget=get_position, fset=set_position)

    #void glfwGetWindowSize(GLFWwindow* window, int* width, int* height);
    @throw_errors
    def get_size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')

        libglfw.glfwGetWindowSize(self._window, width, height)

        return int(width), int(height)

    #void glfwSetWindowSize(GLFWwindow* window, int width, int height);
    @throw_errors
    def set_size(self, width, height):
        libglfw.glfwSetWindowSize(self._window, width, height)

    size = property(fget=get_size, fset=set_size)

    #void glfwGetFramebufferSize(GLFWwindow* window, int* width, int* height);
    @property
    @throw_errors
    def framebuffer_size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')

        libglfw.glfwGetWindowSize(self._window, width, height)

        return int(width), int(height)

    #void glfwIconifyWindow(GLFWwindow* window);
    @throw_errors
    def iconify(self):
        libglfw.glfwIconifyWindow(self._window)

    #void glfwRestoreWindow(GLFWwindow* window);
    @throw_errors
    def restore(self):
        libglfw.glfwRestoreWindow(self._window)

    #void glfwHideWindow(GLFWwindow* window);
    @throw_errors
    def hide(self):
        libglfw.glfwHideWindow(self._window)

    #void glfwShowWindow(GLFWwindow* window);
    @throw_errors
    def show(self):
        libglfw.glfwShowWindow(self._window)


    # TODO
    #GLFWmonitor* glfwGetWindowMonitor(GLFWwindow* window);
    #int glfwGetWindowAttrib(GLFWwindow* window, int attrib);
    #void glfwSetWindowUserPointer(GLFWwindow* window, void* pointer);
    #void* glfwGetWindowUserPointer(GLFWwindow* window);
    #GLFWwindowposfun glfwSetWindowPosCallback(GLFWwindow* window, GLFWwindowposfun cbfun);
    #GLFWwindowsizefun glfwSetWindowSizeCallback(GLFWwindow* window, GLFWwindowsizefun cbfun);
    #GLFWwindowclosefun glfwSetWindowCloseCallback(GLFWwindow* window, GLFWwindowclosefun cbfun);
    #GLFWwindowrefreshfun glfwSetWindowRefreshCallback(GLFWwindow* window, GLFWwindowrefreshfun cbfun);
    #GLFWwindowfocusfun glfwSetWindowFocusCallback(GLFWwindow* window, GLFWwindowfocusfun cbfun);
    #GLFWwindowiconifyfun glfwSetWindowIconifyCallback(GLFWwindow* window, GLFWwindowiconifyfun cbfun);
    #GLFWframebuffersizefun glfwSetFramebufferSizeCallback(GLFWwindow* window, GLFWframebuffersizefun cbfun);
    #int glfwGetInputMode(GLFWwindow* window, int mode);
    #void glfwSetInputMode(GLFWwindow* window, int mode, int value);
    #int glfwGetKey(GLFWwindow* window, int key);
    #int glfwGetMouseButton(GLFWwindow* window, int button);
    #void glfwGetCursorPos(GLFWwindow* window, double* xpos, double* ypos);
    #void glfwSetCursorPos(GLFWwindow* window, double xpos, double ypos);
    #GLFWkeyfun glfwSetKeyCallback(GLFWwindow* window, GLFWkeyfun cbfun);
    #GLFWcharfun glfwSetCharCallback(GLFWwindow* window, GLFWcharfun cbfun);
    #GLFWmousebuttonfun glfwSetMouseButtonCallback(GLFWwindow* window, GLFWmousebuttonfun cbfun);
    #GLFWcursorposfun glfwSetCursorPosCallback(GLFWwindow* window, GLFWcursorposfun cbfun);
    #GLFWcursorenterfun glfwSetCursorEnterCallback(GLFWwindow* window, GLFWcursorenterfun cbfun);
    #GLFWscrollfun glfwSetScrollCallback(GLFWwindow* window, GLFWscrollfun cbfun);

    #void glfwSetClipboardString(GLFWwindow* window, const char* string);
    #const char* glfwGetClipboardString(GLFWwindow* window);
    #int glfwExtensionSupported(const char* extension);
    #GLFWglproc glfwGetProcAddress(const char* procname);

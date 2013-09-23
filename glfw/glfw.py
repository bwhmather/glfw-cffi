def init():
    if not C.glfwInit():
        raise Exception()
    
#void glfwTerminate(void);
def terminate():
    C.glfwTerminate()

#void glfwGetVersion(int* major, int* minor, int* rev);
# const char* glfwGetVersionString(void);
def get_version(verbose=False):
    if not verbose:
        major = ffi.new('int *')
        minor = ffi.new('int *')
        rev = ffi.new('int *')

        C.glfwGetVersion(major, minor, rev)

        return '{}.{}.{}'.format(major, minor, rev)
    else:
        str(C.glfwGetVersionString()

#GLFWerrorfun glfwSetErrorCallback(GLFWerrorfun cbfun);
# TODO



class Monitor(object):
    def __init__(cmonitor):
        self._monitor = cmonitor

    #void glfwGetMonitorPos(GLFWmonitor* monitor, int* xpos, int* ypos);
    @property
    def position(self):
        x = ffi.new('int *')
        y = ffi.new('int *')
    
        C.glfwGetMonitorPos(self._monitor, x, y)
    
        return int(x), int(y)
    
    
    #void glfwGetMonitorPhysicalSize(GLFWmonitor* monitor, int* width, int* height);
    @property
    def size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')
    
        C.glfwGetMonitorPos(self._monitor, width, height)
    
        return int(width), int(height)
    

    #const char* glfwGetMonitorName(GLFWmonitor* monitor);
    @property
    def name(self):
        return str(C.glfwGetMonitorName(self._monitor))

    #GLFWmonitorfun glfwSetMonitorCallback(GLFWmonitorfun cbfun);
    # TODO

    #const GLFWvidmode* glfwGetVideoModes(GLFWmonitor* monitor, int* count);
    #const GLFWvidmode* glfwGetVideoMode(GLFWmonitor* monitor);
    #void glfwSetGamma(GLFWmonitor* monitor, float gamma);
    #const GLFWgammaramp* glfwGetGammaRamp(GLFWmonitor* monitor);
    #void glfwSetGammaRamp(GLFWmonitor* monitor, const GLFWgammaramp* ramp);


#GLFWmonitor** glfwGetMonitors(int* count);
def get_monitors():
    raise NotImplementedError()


#GLFWmonitor* glfwGetPrimaryMonitor(void);
def get_primary_monitor():
    return C.glfwGetPrimaryMonitor()

class Window(object):
#GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);
    def __init__(self, width, height, title, monitor=None):
        self._title = str(title)
        if not isinstance(title, ffi.CData):
            title = ffi.new('const char *', title)

        self._window = glfwCreateWindow(width, height, title, monitor._monitor);

    #void glfwMakeContextCurrent(GLFWwindow* window);
    def activate(self):
        C.glfwMakeContextCurrent(self._window)

    #void glfwSwapBuffers(GLFWwindow* window);
    def swap_buffers(self):
        C.glfwSwapBuffers(self._window);


    #void glfwDefaultWindowHints(void);
    #void glfwWindowHint(int target, int hint);
    #GLFWwindow* glfwCreateWindow(int width, int height, const char* title, GLFWmonitor* monitor, GLFWwindow* share);


    # TODO
    #void glfwDestroyWindow(GLFWwindow* window);
    #int glfwWindowShouldClose(GLFWwindow* window);
    #void glfwSetWindowShouldClose(GLFWwindow* window, int value);


    #void glfwSetWindowTitle(GLFWwindow* window, const char* title);
    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = str(title)
        if not isinstance(title, ffi.CData):
            title = ffi.new('const char *', title)
        C.glfwSetWindowTitle(self._window, title)

    title = property(fget=get_title, fset=set_title)


    #void glfwGetWindowPos(GLFWwindow* window, int* xpos, int* ypos);
    def get_position(self):
        x = ffi.new('int *')
        y = ffi.new('int *')
    
        C.glfwGetWindowPos(self._window, x, y)
    
        return int(x), int(y)

    #void glfwSetWindowPos(GLFWwindow* window, int xpos, int ypos);
    def set_position(self, x, y):
        C.glfwSetWindowSize(self._window, x, y)

    position = property(fget=get_position, fset=set_position)


    #void glfwGetWindowSize(GLFWwindow* window, int* width, int* height);
    def get_size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')
    
        C.glfwGetWindowSize(self._window, width, height)
    
        return int(window), int(height)

    #void glfwSetWindowSize(GLFWwindow* window, int width, int height);
    def set_size(self, width, height):
        C.glfwSetWindowSize(self._window, width, height)

    size = property(fget=get_size, fset=set_size)

    #void glfwGetFramebufferSize(GLFWwindow* window, int* width, int* height);
    @property
    def framebuffer_size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')
    
        C.glfwGetWindowSize(self._window, width, height)
    
        return int(window), int(height)


    #void glfwIconifyWindow(GLFWwindow* window);
    def iconify(self):
        C.glfwIconifyWindow(self._window)

    #void glfwRestoreWindow(GLFWwindow* window);
    def restore(self):
        C.glfwRestoreWindow(self._window)

    #void glfwHideWindow(GLFWwindow* window);
    def hide(self):
        C.glfwHideWindow(self._window)

    #void glfwShowWindow(GLFWwindow* window);
    def show(self):
        C.glfwShowWindow(self._window)


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

#GLFWwindow* glfwGetCurrentContext(void);
# TODO sort of internal
def get_current_window():
    return C.glfwGetCurrentContext()

#void glfwPollEvents(void);
def poll_events():
    C.glfwPollEvents()

#void glfwWaitEvents(void);
def wait_events():
    C.glfwWaitEvents()

class Joystick(object):
    pass
    #int glfwJoystickPresent(int joy);
    #const float* glfwGetJoystickAxes(int joy, int* count);
    #const unsigned char* glfwGetJoystickButtons(int joy, int* count);
    #const char* glfwGetJoystickName(int joy);

#void glfwSetClipboardString(GLFWwindow* window, const char* string);
#const char* glfwGetClipboardString(GLFWwindow* window);
#double glfwGetTime(void);
#void glfwSetTime(double time);
#void glfwSwapInterval(int interval);
#int glfwExtensionSupported(const char* extension);
#GLFWglproc glfwGetProcAddress(const char* procname);

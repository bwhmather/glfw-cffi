from glfw._glfw import ffi, libglfw


__all__ = ['Monitor', 'get_monitors', 'get_primary_monitor']


class Monitor(object):
    def __init__(self, monitor):
        self._monitor = monitor

    #void glfwGetMonitorPos(GLFWmonitor* monitor, int* xpos, int* ypos);
    @property
    def position(self):
        x = ffi.new('int *')
        y = ffi.new('int *')

        libglfw.glfwGetMonitorPos(self._monitor, x, y)

        return int(x), int(y)

    #void glfwGetMonitorPhysicalSize(GLFWmonitor* monitor, int* width, int* height);
    @property
    def size(self):
        width = ffi.new('int *')
        height = ffi.new('int *')

        libglfw.glfwGetMonitorPos(self._monitor, width, height)

        return int(width), int(height)

    #const char* glfwGetMonitorName(GLFWmonitor* monitor);
    @property
    def name(self):
        return str(libglfw.glfwGetMonitorName(self._monitor))

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
    # TODO singletons
    return Monitor(libglfw.glfwGetPrimaryMonitor())

from glfw._glfw import ffi, libglfw


class Joystick(object):
    pass
    #int glfwJoystickPresent(int joy);
    #const float* glfwGetJoystickAxes(int joy, int* count);
    #const unsigned char* glfwGetJoystickButtons(int joy, int* count);
    #const char* glfwGetJoystickName(int joy);

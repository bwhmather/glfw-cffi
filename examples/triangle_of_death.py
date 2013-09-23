import glfw

try:

    glfw.init()

    # Create a windowed mode window and its OpenGL context
    window = glfw.Window(640, 480, "Hello World")

    # Make the window's context current
    window.make_current()

    # Loop until the user closes the window 
    while not window.should_close():
        # Render here

        # Swap front and back buffers
        window.swap_buffers()

        # Poll for and process events
        glfw.poll_events()

finally:
    glfw.terminate()

#!/usr/bin/bash

function do_test
{
    reset
    pep8 glfw
    pyflakes glfw
    nostests glfw
}

do_test
while true; do
    find . -name '*.py' -exec inotifywait -e MOVE_SELF {} +;
    do_test;
done

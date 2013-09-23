import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="glew-cffi",
    version="0.1",
    author="Ben Mather",
    author_email="bwhmather@bwhmather.com",
    description="cffi bindings to glfw opengl windowing toolkit",
    license="MIT",
    url="https://github.com/bwhmather/glfw-cffi",
    packages=find_packages(exclude=['tests']),
    package_dir={'glfw': 'glfw'},
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    test_suite='glfw.tests',
    install_requires=[
        'cffi==0.7',
    ],
)

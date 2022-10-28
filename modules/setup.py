from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension("compute",
              sources=["compute.pyx"],
              libraries=["m"] # Unix-like specific
              )
]

setup(name="compute",
      ext_modules=cythonize(ext_modules, compiler_directives={'language_level' : "3"}))
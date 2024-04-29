from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name="AyuPon",
    ext_modules=cythonize(["AyuPon/math.pyx"]),
    packages=find_packages(),
    include_dirs=['AyuPon'],
    extra_compile_args=["-lm"] 
)

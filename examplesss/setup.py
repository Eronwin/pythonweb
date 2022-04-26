from distutils.core import setup,Extension



Example=Extension("_example",sources=["example.cpp","example_wrap.cxx"])

setup(
    name="example",
    version="0.1",
    author="kekao",
    description="example_el_search",
    ext_modules=[Example],
    py_modules=["example"],)
from distutils.core import setup,Extension


matching=Extension("_matching",sources=["matching.cpp","matching_wrap.cxx"])

setup(
    name="matching",
    version="0.1",
    author="kekao",
    description="example_el_search",
    ext_modules=[matching],
    py_modules=["matching"],)
from distutils.core import setup
import py2exe
 
setup(
    windows=[{"script":"testmain.py"}],
    options={"py2exe": {"includes":["openpyxl"]}}
)
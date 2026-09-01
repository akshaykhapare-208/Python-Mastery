# A module is a file containing code written by somebody else which can be imported and used in our programs. [ Flask , Numpy ...etc]

# Pip is the package manager for Python. You can use pip to install external modules on your system.
'''
-- > Types of Modules
There are two types of modules in Python.
1) Builtin Modules are preinstalled with Python.
2) External Modules need to be installed using
pip.
Examples of builtin modules are os and random. Examples of external modules are tensorflow and
flask.  '''

# We install The Module [pip install pyjokes]

import pyjokes

print(pyjokes.get_joke())
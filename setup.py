#!/usr/bin/env python
from distutils.core import setup

VERSION = "1.5.2"

setup(
    name = "PySocks",
    version = VERSION,
    description = "A Python SOCKS client module",
    url = "https://github.com/Anorov/PySocks",
    license = "BSD",
    author_email = "anorov.vorona@gmail.com",
    keywords = ["socks", "proxy"],
    py_modules=["socks", "sockshandler"]
)


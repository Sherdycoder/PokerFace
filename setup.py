# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:09:32 2016

@author: Jonathan Yancey
"""


import sys
from cx_Freeze import setup, Executable


setup(
    name = "Sherdycoder",
    version = "1.0",
    description = "Set facial expression derivative == 0",
    options = {"build_exe": {"packages": ["numpy.lib.format"]}},
    executables = [Executable("PokerFace.py", base = "Win32GUI")])

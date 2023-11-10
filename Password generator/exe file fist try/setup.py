import sys
from cx_Freeze import setup, Executable

setup(
    name = "Pass_Gen",
    version = "1.0",
    description = "Password gen",
    executables = [Executable("password_generator.py")]
)

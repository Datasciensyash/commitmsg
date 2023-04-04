from pathlib import Path

from setuptools import find_packages, setup

THIS_DIR = Path(__file__).parent


setup(
    name="commitmsg",
    version="0.1",
    author="Datasciensyash",
    packages=find_packages(),
    python_requires="~=3.8",
    install_requires=[
        "openai",
        "gitpython",
    ],
    entry_points={
        "console_scripts": [
        ],
    }
)

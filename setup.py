from setuptools import setup, find_packages

setup(
    name="depwatch",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "typer",
        "pyyaml",
        "toml",
    ],
    entry_points={
        "console_scripts": [
            "depwatch=depwatch.main:main",
        ],
    },
)
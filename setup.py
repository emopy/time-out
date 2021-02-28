from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "timeout = my_project.__main__:main"
        ]
    },
)

from setuptools import find_packages, setup

setup(
    name="mon",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mon=mon.main:main",
        ],
    },
    install_requires=[],
    include_package_data=True,  # Ensures non-Python files (like the SQLite DB) are included

)
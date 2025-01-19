from setuptools import setup, find_packages

setup(
    name="ascii-art-generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
            'ascii-art-generator=ascii_art:main',
        ],
    },
)

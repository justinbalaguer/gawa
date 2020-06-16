from setuptools import setup
setup(
    name = 'gawa',
    version = '1.0.0',
    packages = ['gawa'],
    entry_points = {
        'console_scripts': [
            'gawa = gawa.__main__:main'
        ]
    })
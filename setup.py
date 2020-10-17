from setuptools import setup
setup(
    name = 'themis',
    version = '0.1.0',
    packages = ['themis'],
    entry_points = {
        'console_scripts': [
            'themis = themis.__main__:main'
        ]
    })
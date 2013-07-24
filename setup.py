from setuptools import setup

setup(
    name='Python Challenge',
    version='1.0',
    long_description=__doc__,
    packages=['python_challenge'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'PyMongo', 'Flask-PyMongo', 'Flask-wtf']
)

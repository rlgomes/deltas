"""
setup.py
"""
from setuptools import setup, find_packages

__VERSION = '0.1'

setup(
    name='deltas',
    version=__VERSION,
    author='Rodney Gomes',
    author_email='rodneygomes@gmail.com',
    url='https://github.com/rlgomes/deltas',
    install_requires=[],
    tests_require=[
        'robber==1.0.1'
    ],
    test_suite='test',
    keywords=['date', 'durations', 'timedelta'],
    py_modules=['deltas'],
    packages=find_packages(exclude=['test']),

    license='MIT',
    description='Human friendly context aware duration parsing library',
    long_description=open('README.md').read(),
)

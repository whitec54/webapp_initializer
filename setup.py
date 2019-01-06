"""
webapp_initializer python package configuration

Cam White <camwhite@umich.edu>
"""

from setuptools import setup

setup(
    name='webapp_initializer',
    version='0.1.0',
    packages=['webapp_initializer'],
    include_package_data=True,
    install_requires=[
        'astroid==2.1.0',
        'Click==7.0',
        'isort==4.3.4',
        'Jinja2==2.10',
        'lazy-object-proxy==1.3.1',
        'MarkupSafe==1.1.0',
        'mccabe==0.6.1',
        'pycodestyle==2.3.1',
        'pydocstyle==2.0.0',
        'pylint==2.1.1',
        'sh==1.12.14',
        'six==1.12.0',
        'snowballstemmer==1.2.1',
        'webapp-initializer==0.1.0',
        'wrapt==1.10.11'
    ],
    entry_points={
        'console_scripts': [
            'wapi = webapp_initializer.__main__:main'
        ]
    },
)

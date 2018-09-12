#!/usr/bin/env python
from setuptools import find_packages, setup
import io
import os

NAME = 'hunspell_serializable'
DESCRIPTION = 'Wrapper for pyhunspell that makes HunSpell class serializable.'
URL = 'https://github.com/rominf/pyhunspell_serializable'
EMAIL = 'infroma@gmail.com'
AUTHOR = 'Roman Inflianskas'
VERSION = None

REQUIRED = ['hunspell']
here = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=REQUIRED,
    include_package_data=True,
    license='LGPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
    ],
)

# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Aniket Gole",
    author_email="roshan3133@gmail.com",
    maintainer='aniket gole',
    maintainer_email='roshan3133@gmail.com',
    name='helloworld',
    version='0.1',
    description='Django hello world example ',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/roshan3133/django_helloworld',
    license='GPL',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django==1.9.4',
    ],
    packages=find_packages(exclude=["project","project.*"]),
    include_package_data=True,
    zip_safe = False
)

from setuptools import setup

setup(
    name='django-metadata',
    version='1.2',
    url='https://github.com/rwizi/django-metadata',
    author='Rafael Sierra',
    author_email='eu@rafaelsdm.com',
    license='Free Use',
    packages=['metadata'],
    include_package_data=True,
    description='This is a simple addon to your models, with this package you can add metadata to any of your models',
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Freeware",
        "Programming Language :: Python :: 2.7",
    ],
)

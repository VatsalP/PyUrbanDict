from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyUrbanDict',
    version='0.1.0',

    description='Python wrapper for urbandictionary api',
    long_description=long_description,

    url='https://github.com/VatsalP/PyUrbanDict',

    author='Mitesh Shah, Vatsal Parekh',
    author_email='vatsalbparekh@gmail.com',

    license='MIT',

    classifiers=[
                'Development Status :: 3 - Alpha',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'Programming Language :: Python :: 3.5',
    ],
    keywords='api urbandictionary wrapper',
    packages=find_packages(exclude=['pyurbandicttests']),
    install_requires=['requests'],
    zip_safe=True,
)

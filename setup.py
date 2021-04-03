from setuptools import setup, find_packages
from os import path

classifiers = [
    'Development Status :: 6 - Mature',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3',
    'Topic :: Internet',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Testing',
    'Topic :: Text Processing',
    'Topic :: Utilities'
]

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()


# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='Goje',
    version='0.0.4',
    description='Unofficial Library for Scrapping Rotten Tomato.',
    long_description=long_description,
    url='https://faze.li',
    author='Ali Fazeli',
    author_email='a.fazeli95@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='scrapper',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4', 'lxml'],
    setup_requires=['setuptools>=41.0.1','wheel>=0.33.4','pypandoc'])

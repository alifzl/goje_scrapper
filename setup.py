from setuptools import setup, find_packages

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

setup(
    name='Goje',
    version='0.0.1',
    description='Unofficial Library for Scrapping Rotten Tomato.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://faze.li',
    author='Ali Fazeli',
    author_email='a.fazeli95@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='scrapper',
    packages=find_packages(),
    install_requires=['requests','beautifulsoup4']
)
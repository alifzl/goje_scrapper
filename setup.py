from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Goje',
    version='0.0.1',
    description='Unofficial Library for Scrapping rotten tomato.',
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
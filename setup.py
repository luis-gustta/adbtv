from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A simple ADB package'

setup(
    name="adbtv",
    version=VERSION,
    description=DESCRIPTION,
    author="Luis Gustavo Lang Gaiato",
    author_email="lang.gaiato@ufrgs.br",
    license='MIT',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=["typing"],
    keywords=['adb','androidtv'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)

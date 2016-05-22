from distutils.core import setup

setup(
    name='PySAF',
    version='1.0.0',
    author='Christopher Starcher',
    author_email='christopher.starcher@ttu.edu',
    packages=['pysaf', 'pysaf.test'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Creates Simple Archive Format packages for upload to DSpace.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Python >= 3.5.1"
    ],
)

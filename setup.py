import setuptools
import universalparser

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='sample_package',
    version=universalparser.__version__,
    packages=setuptools.find_packages(),
    install_requires=install_requires
 )
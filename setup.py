from setuptools import setup, find_packages

setup(
    name='potential_flow',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    author='John Parks',
    description='Basic implentation of potential flow structures',
)

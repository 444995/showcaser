from setuptools import setup, find_packages

setup(
    name='showcaser',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'showcaser=showcaser.__main__:main',
        ]
    }
)

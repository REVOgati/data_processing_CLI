from setuptools import setup

setup(
    name='DATA_PROCESSING_CLI',
    version='0.1',
    py_modules=['data_processor'],
    install_requires=[
        'pandas', 
        # argparse is optional for Python 3.2+ as it is part of the standard library.
    ],
    entry_points={
        'console_scripts': [
            'data-processor=data_processor:main',
        ],
    },
)

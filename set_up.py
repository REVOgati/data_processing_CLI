from setuptools import setup

setup(
    name= 'DATA_PROCESSING_CLI', 
    version= '0.1',
    py_modules= ['data_processor',],
    install_requires= ['pandas', 
                       'argparse']
    """N/B: argparse is optional for python 3.2+ versions
        as it is automatically installed with the Python Standard Library """
    entrypoints = [
        '''
        [console_scripts]
        data-processor=data_processor:main
        '''
    ]
     
)
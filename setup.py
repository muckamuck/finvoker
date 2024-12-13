from setuptools import setup, find_packages

setup(
    name='LambdaUtil',
    version='0.0.1',
    packages=find_packages(),
    description='Python Lambda Utility',
    author='Duke P. Takle',
    author_email='duke.takle@gmail.com',
    install_requires=[
        'boto3',
        'Click'
    ],
    entry_points='''
        [console_scripts]
        finvoker=finvoker.command:cli
    '''
)
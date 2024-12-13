'''
The command line interface to Lambda Utility
'''
# pylint: disable=line-too-long
import sys
import json
import logging

import click
from finvoker.utility import invoke_the_thing

logging.basicConfig(
    level=logging.WARNING,
    stream=sys.stdout,
    format='[%(levelname)s] %(asctime)s (%(module)s) %(message)s',
    datefmt='%Y/%m/%d-%H:%M:%S'
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@click.group()
@click.version_option(version='0.1.0')
def cli():
    '''
    The command line interface to Lambda Utility
    '''


@cli.command()
@click.option('-n', '--name', help='name of the lambda', required=True)
@click.option('-f', '--datafile', help='data file for the event', required=False)
def invoke(name, datafile):
    '''
    Invoke a function
    '''
    the_data = None
    try:
        if datafile:
            with open(datafile, 'r') as stuff:
                the_data = json.load(stuff)
        else:
            the_data = {
                'event_data': None,
                'invoker': 'finvoker - v0.1.0'
            }
    except Exception as wtf:
        logger.error(wtf, exc_info=True)
        sys.exit(1)

    invoke_the_thing(name, the_data)

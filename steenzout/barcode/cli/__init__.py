# -*- coding: utf-8 -*-
"""Command-line tool package."""

import click
import logging

from steenzout import barcode
from steenzout.barcode import writer


try:
    import PIL
except ImportError:
    PIL = None

if PIL is not None:
    IMG_FORMATS = ('BMP', 'EPS', 'GIF', 'JPEG', 'MSP', 'PCX', 'PNG', 'SVG', 'TIFF', 'XBM')
else:
    IMG_FORMATS = ('EPS', 'SVG')


LOGGER = logging.getLogger(__name__)


@click.group()
@click.version_option(version=barcode.__version__)
def cli():
    pass


@cli.command()
@click.option('-v', '--verbose', 'verbosity', count=True, help='Enables verbosity.')
@click.option('-e', '--encoding', 'encoding', default='code39', type=click.Choice(barcode.encodings()))
@click.option('-f', '--format', 'format', default='SVG', type=click.Choice(IMG_FORMATS))
@click.option('-u', '--unit', 'unit', type=click.STRING)
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def generate(verbosity, encoding, format, unit, input, output):
    """Generates the bar code."""
    LOGGER.debug('generate(): %s, %s, %s, %s, %s, %s', verbosity, encoding, format, unit, input, output)

    if format == 'SVG':
        opts = dict(compress=False)
        writer_instance = writer.SVG()
    else:
        opts = dict(format=format)
        writer_instance = writer.ImageWriter()

    barcode.generate(encoding, input.read(), writer_instance, output, opts)


@cli.command()
def encodings():
    """List the available bar codes."""
    LOGGER.debug('formats()')

    for fmt in barcode.encodings():
        click.echo(fmt)


@cli.command()
def formats():
    """List the available image formats."""
    LOGGER.debug('formats()')

    for fmt in IMG_FORMATS:
        click.echo(fmt)

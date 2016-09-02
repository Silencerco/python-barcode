Command-line interface
======================

The install script detects your Python version and
adds the major and minor Python version number to the executable script.

For example, on Python 2.7,
the command-line interface tool will be
`py27-barcode`.


Commands
--------

Usage::

   $ py27-barcode --help
   Usage: py27-barcode [OPTIONS] COMMAND [ARGS]...

   Options:
     --version  Show the version and exit.
     --help     Show this message and exit.

   Commands:
     encodings  List the available bar codes.
     formats    List the available image formats.
     generate   Generates the bar code.

Generate::

   $ py27-barcode generate --help
   Usage: py27-barcode generate [OPTIONS] INPUT OUTPUT

     Generates the bar code.

   Options:
     -v, --verbose                   Enables verbosity.
     -e, --encoding [code128|code39|ean|ean13|ean8|gs1|gtin|isbn|isbn10|isbn13|issn|jan|pzn|upc|upca]
     -f, --format [BMP|EPS|GIF|JPEG|MSP|PCX|PNG|SVG|TIFF|XBM]
     -u, --unit TEXT
     --help                          Show this message and exit.


The number of output formats available will depend if you installed `PIL`::

   $ pip install steenzout.barcode[image]

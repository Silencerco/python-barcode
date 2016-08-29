# -*- coding: utf-8 -*-
"""ISXN module.

:Provided barcodes: ISBN-13, ISBN-10, ISSN

This module provides some special codes, which are no standalone bar codes.

All codes where transformed to EAN-13 barcodes.

In every case, the checksum is new calculated.

Example::

    >>> from steenzout.barcode import get_barcode
    >>> ISBN = get_barcode('isbn10')
    >>> isbn = ISBN('0132354187')
    >>> unicode(isbn)
    u'0132354187'
    >>> isbn.get_fullcode()
    u'9780132354189'
    >>> # Test with wrong checksum
    >>> isbn = ISBN('0132354180')
    >>> unicode(isbn)
    u'0132354187'
"""

from __future__ import unicode_literals

from .ean import EAN13
from .errors import *

__docformat__ = 'restructuredtext en'


class ISBN13(EAN13):
    """Class for ISBN-13 bar codes.

    Args:
        isbn (str): isbn number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'ISBN-13'

    def __init__(self, isbn, writer=None):
        self.isbn13 = isbn.replace('-', '')
        if isbn[:3] not in ('978', '979'):
            raise WrongCountryCodeError('ISBN must start with 978 or 979.')

        super(ISBN13, self).__init__(self.isbn13, writer)


class ISBN10(ISBN13):
    """Class for ISBN-10 bar codes.

    This code is rendered as EAN-13 by prefixing it with 978.

    Args:
        isbn (str): isbn number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'ISBN-10'

    digits = 9

    def __init__(self, isbn, writer=None):
        isbn = isbn.replace('-', '')[:InternationalStandardBookNumber10.digits]
        self.isbn10 = isbn
        self.isbn10 = '{0}{1}'.format(isbn, self._calculate_checksum())

        super(ISBN10, self).__init__('978' + isbn, writer)

    def _calculate_checksum(self):
        tmp = sum([x * int(y) for x, y in enumerate(self.isbn10[:9],
                                                    start=1)]) % 11
        if tmp == 10:
            return 'X'
        else:
            return tmp

    def __unicode__(self):
        return self.isbn10

    __str__ = __unicode__


class ISSN(EAN13):
    """Class for ISSN bar codes.

    This code is rendered as EAN-13 by prefixing it with 977 and
    adding 00 between code and checksum.

    Args:
        issn (str): issn number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'ISSN'

    digits = 7

    def __init__(self, issn, writer=None):
        self.issn = issn.replace('-', '')[:InternationalStandardSerialNumber.digits]
        self.issn = '{0}{1}'.format(issn, self._calculate_checksum())

        super(ISSN, self).__init__(self.make_ean(), writer)

    def _calculate_checksum(self):
        tmp = 11 - sum([x * int(y) for x, y in
                        enumerate(reversed(self.issn[:7]), start=2)]) % 11
        if tmp == 10:
            return 'X'
        else:
            return tmp

    def make_ean(self):
        return '977{0}00{1}'.format(self.issn[:7], self._calculate_checksum())

    def __unicode__(self):
        return self.issn

    __str__ = __unicode__


# Shortcuts
InternationalStandardBookNumber13 = ISBN13
InternationalStandardBookNumber10 = ISBN10
InternationalStandardSerialNumber = ISSN

# -*- coding: utf-8 -*-
"""Module: barcode.ean

:Provided barcodes: EAN-13, EAN-8, JAN
"""

from __future__ import unicode_literals

from .base import Barcode
from .charsets import ean as _ean
from .errors import IllegalCharacterError, WrongCountryCodeError

from functools import reduce


# EAN13 Specs (all sizes in mm)
SIZES = dict(SC0=0.27, SC1=0.297, SC2=0.33, SC3=0.363, SC4=0.396, SC5=0.445,
             SC6=0.495, SC7=0.544, SC8=0.61, SC9=0.66)


class EAN13(Barcode):
    """Class for EAN13 bar codes.

    Args:
        ean (str): the EAN number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'EAN-13'

    digits = 12

    def __init__(self, ean, writer=None):
        ean = ean[:self.digits]
        if not ean.isdigit():
            raise IllegalCharacterError('EAN code can only contain numbers.')
        self.ean = '%s%s' % (ean, self.__class__.calculate_checksum(ean))
        self.writer = writer or Barcode.default_writer()

    def __unicode__(self):
        return self.ean

    __str__ = __unicode__

    @staticmethod
    def calculate_checksum(ean):
        """Calculates the checksum for EAN13-Code.

        Args:
            ean (str):

        Returns:
            (integer): the checksum for `self.ean`.
        """
        def sum_(x, y):
            return int(x) + int(y)

        evensum = reduce(sum_, ean[::2])
        oddsum = reduce(sum_, ean[1::2])
        return (10 - ((evensum + oddsum * 3) % 10)) % 10

    def get_fullcode(self):
        return self.ean

    def build(self):
        """Builds the barcode pattern from `self.ean`.

        Returns:
            (str): The pattern as string.
        """
        code = _ean.EDGE[:]
        pattern = _ean.LEFT_PATTERN[int(self.ean[0])]
        for i, number in enumerate(self.ean[1:7]):
            code += _ean.CODES[pattern[i]][int(number)]
        code += _ean.MIDDLE
        for number in self.ean[7:]:
            code += _ean.CODES['C'][int(number)]
        code += _ean.EDGE
        return [code]

    def to_ascii(self):
        """Returns an ascii representation of the barcode.

        Returns:
            (str): ascii representation of the barcode.
        """
        code = self.build()
        for i, line in enumerate(code):
            code[i] = line.replace('1', '|').replace('0', ' ')
        return '\n'.join(code)

    def render(self, writer_options=None):
        options = dict(module_width=SIZES['SC2'])
        options.update(writer_options or {})
        return Barcode.render(self, options)


class JAN(EAN13):
    """Class for JAN bar codes.

    Args:
        jan (str): the jan number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'JAN'

    valid_country_codes = list(range(450, 460)) + list(range(490, 500))

    def __init__(self, jan, writer=None):
        if int(jan[:3]) not in JapanArticleNumber.valid_country_codes:
            raise WrongCountryCodeError("Country code isn't between 450-460 "
                                        "or 490-500.")
        super(JAN, self).__init__(jan, writer)


class EAN8(EAN13):
    """Class for EAN-8 bar codes.

    See :py:class:`EAN13` for details.

    :parameters:
        ean (str): ean number.
        writer (:py:class:`.writer.BaseWriter`): instance of writer class to render the bar code.
    """

    name = 'EAN-8'

    digits = 7

    def __init__(self, ean, writer=None):
        super(EAN8, self).__init__(ean, writer)

    @staticmethod
    def calculate_checksum(ean):
        """Calculates the checksum for EAN8-Code.

        Returns:
            (int): checksum for `self.ean`.
        """
        def sum_(x, y):
            return int(x) + int(y)

        evensum = reduce(sum_, ean[::2])
        oddsum = reduce(sum_, ean[1::2])
        return (10 - ((evensum * 3 + oddsum) % 10)) % 10

    def build(self):
        """Builds the barcode pattern from `self.ean`.

        Returns:
            (str): string representation of the pattern.
        """
        code = _ean.EDGE[:]
        for number in self.ean[:4]:
            code += _ean.CODES['A'][int(number)]
        code += _ean.MIDDLE
        for number in self.ean[4:]:
            code += _ean.CODES['C'][int(number)]
        code += _ean.EDGE
        return [code]


# Shortcuts
EuropeanArticleNumber13 = EAN13
EuropeanArticleNumber8 = EAN8
JapanArticleNumber = JAN

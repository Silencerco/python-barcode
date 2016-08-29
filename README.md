# steenzout.barcode

This repository is a fork of:
- [viivakoodi][viivakoodi]
- [pyBarcode][pyBarcode]

This library provides the ability to create bar codes.

The bar codes are created as SVG objects.


## Installation

```
$ pip install steenzout.barcode
```


## Bar codes

- EAN-8
- EAN-13
- UPC-A
- JAN
- ISBN-10
- ISBN-13
- ISSN
- Code 39
- Code 128
- PZN


## Usage

```
>>> from steenzout import barcode
>>> barcode.PROVIDED_BARCODES
[u'code39', u'code128', u'ean', u'ean13', u'ean8', u'gs1', u'gtin',
 u'isbn', u'isbn10', u'isbn13', u'issn', u'jan', u'pzn', u'upc', u'upca']
>>> EAN = barcode.get_barcode_class('ean13')
>>> EAN
<class 'barcode.ean.EuropeanArticleNumber13'>
>>> ean = EAN(u'5901234123457')
>>> ean
<barcode.ean.EuropeanArticleNumber13 object at 0x00BE98F0>
>>> fullname = ean.save('ean13_barcode')
>>> fullname
u'ean13_barcode.svg'
# Example with PNG
>>> from barcode.writer import ImageWriter
>>> ean = EAN(u'5901234123457', writer=ImageWriter())
>>> fullname = ean.save('ean13_barcode')
u'ean13_barcode.png'
# New in v0.4.2
>>> from StringIO import StringIO
>>> fp = StringIO()
>>> ean.write(fp)
# or
>>> f = open('/my/new/file', 'wb')
>>> ean.write(f) # PIL (ImageWriter) produces RAW format here
# New in v0.5.0
>>> from barcode import generate
>>> name = generate('EAN13', u'5901234123457', output='barcode_svg')
>>> name
u'barcode_svg.svg'
# with file like object
>>> fp = StringIO()
>>> generate('EAN13', u'5901234123457', writer=ImageWriter(), output=fp)
>>>
```

Now open ean13_barcode
[svg|png] in a graphic app or simply in your browser and
see the created barcode. That's it.


## Commandline

```
$ pybarcode{2,3} create "My Text" outfile
New barcode saved as outfile.svg.

$ pybarcode{2,3} create -t png "My Text" outfile
New barcode saved as outfile.png.

Try `pybarcode -h` for help.
```


[pyBarcode] https://bitbucket.org/whitie/python-barcode/    "barcode"
[viivakoodi]    https://github.com/kxepal/viivakoodi    "viivakoodi"

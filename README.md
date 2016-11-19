# Philips Hue Python RGB / CIE1931 Converter

RGB conversion tool written in Python for Philips Hue.

```python
In [1]: from rgb_cie import Converter

In [2]: converter = Converter()
		
In [3]: converter.hexToCIE1931('bada55')
Out[3]: [0.3991853917195425, 0.498424689144739]

In [4]: converter.rgbToCIE1931(255, 0, 0)
Out[4]: [0.6484272236872118, 0.330856101472778]

In [5]: converter.getCIEColor()
Out[5]: [0.3706941388849757, 0.19786410488389355]

In [6]: converter.xyToHEX(0.3991853917195425, 0.498424689144739, bri=0.8)
Out[6]: 'e9e860'
```

## Gamuts

The conversion tool support three gamuts: Gamut A, B, and C, [documented here](http://www.developers.meethue.com/documentation/supported-lights).  Use them as follows:

```python
from rgb_cie import Converter
from rgb_cie import GamutA # or GamutB, GamutC

converter = Converter(GamutA)
```

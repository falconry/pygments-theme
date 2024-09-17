import collections

import pytest


class _RGBColor(collections.namedtuple('_RGBColorTuple', ['r', 'g', 'b'])):
    """RGB color tuple."""

    @classmethod
    def parse(cls, value):
        def from_hex(xx):
            return int(xx, 16) / 255.0

        if isinstance(value, cls):
            return value

        assert isinstance(value, str), 'hex RGB color required'

        value = value.strip()
        value = value.lstrip('#')

        assert len(value) == 6, '3 hex color bytes required'

        return cls(
            from_hex(value[0:2]), from_hex(value[2:4]), from_hex(value[4:6])
        )

    @property
    def relative_luminance(self):
        def to_srgb(value):
            if value <= 0.04045:
                return value / 12.92
            else:
                return ((value + 0.055) / 1.055) ** 2.4

        r_ = to_srgb(self.r)
        g_ = to_srgb(self.g)
        b_ = to_srgb(self.b)
        return 0.2126 * r_ + 0.7152 * g_ + 0.0722 * b_

    def contrast_to(self, other):
        lum1 = self.relative_luminance
        lum2 = other.relative_luminance

        if lum1 < lum2:
            lum1, lum2 = lum2, lum1

        return (lum1 + 0.05) / (lum2 + 0.05)


class _ColorContrast:
    """
    Color contrast checker.

    Inspired by, and some implementation ideas borrowed from,
    https://github.com/Quansight-Labs/accessible-pygments and the now-defunct
    https://github.com/gsnedders/wcag-contrast-ratio/.
    """

    def __init__(self, color1, color2):
        color1 = _RGBColor.parse(color1)
        color2 = _RGBColor.parse(color2)
        self._contrast = color1.contrast_to(color2)

    def as_wcag_normal_text(self):
        if self._contrast >= 7.0:
            return 'AAA'
        elif self._contrast >= 4.5:
            return 'AA'
        else:
            return ''

    def as_wcag_large_text(self):
        if self._contrast >= 4.5:
            return 'AAA'
        elif self._contrast >= 3.0:
            return 'AA'
        else:
            return ''


@pytest.fixture()
def contrast():
    def _compute(color1, color2):
        return _ColorContrast(color1, color2).as_wcag_normal_text()

    return _compute

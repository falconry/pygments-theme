import pytest

from falconry_pygments_theme.light import Colors


_color_names = sorted(
    name
    for name in dir(Colors)
    if not (name.startswith('_') or name == 'light')
)


@pytest.mark.parametrize('color_name', _color_names)
def test_contrast(contrast, color_name):
    value = getattr(Colors, color_name)
    assert contrast(value, Colors.light) >= 'AA'

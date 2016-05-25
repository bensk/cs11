class Color(object):
    """Represents a color"""

DoodooBrown = Color()
PukeGreen = Color()
SK_Pink = Color()
# 204,133,51
DoodooBrown.r = 204
DoodooBrown.g = 133
DoodooBrown.b = 51

PukeGreen.r = 102
PukeGreen.g = 102
PukeGreen.b = 0

SK_Pink.r = 255
SK_Pink.g = 67
SK_Pink.b = 150

def add_color(color1,color2):
    r = (color1.r+color2.r)/2
    print r

add_color(PukeGreen,SK_Pink)
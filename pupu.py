from __future__ import print_function
import zlib, binascii

def draw_pupu():
    print(zlib.decompress(binascii.a2b_base64("eJzdlDsWgCAMBPucgjr3P6CFPM1nDSShkgrXzDyCCI384HtQmSzB3ICZj9EzaEnO9dLqq6WS+9Fz6b2NbLFKla66LKkyoq/tEO9W/8OXYrGAPcyBu5hHM6Rhc6iGs6yE02yXFriKvQ37ET4fROSCEDeTYQOEg5rhAsuH+JyihR3GYckSfwWMilz3QPAoVOaagReDddjULy06o1Q9vn929CTo05YMDQU44kVBzXDsTs8IiC5vJpnU")))

if __name__ == '__main__':
    draw_pupu()

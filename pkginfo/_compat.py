try:
    u = unicode
except NameError: #pragma NO COVER Python >= 3.0
    u = str
    b = bytes
else: #pragma NO COVER Python < 3.0
    b = str


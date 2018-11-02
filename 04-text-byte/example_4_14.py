import unicodedata
import string

def shave_marks(txt):
    """drop all makrs"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

if __name__ == '__main__':
    print(shave_marks('cafe\u0301'))

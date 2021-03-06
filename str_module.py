import linecache
import sys
import time
import random
random.seed(version=2)


def TextException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return 'EXCEPTION IN ({}, LINE {} "{}"):\n{}'.format(filename, lineno, line.strip(), exc_obj)



# check if txt does contain str
def _contain5(text, str):

    iter_txt = 0
    iter_txt_new = 0
    iter_str = 0

    len_txt = len(text)
    len_str = len(str)

    for iter_txt in range(len_txt):

        iter_txt_new = iter_txt
        iter_str = 0

        while iter_txt_new < len_txt and iter_str < len_str and text[iter_txt_new] == str[iter_str]:
            iter_txt_new += 1
            iter_str += 1

        if iter_str == len_str:
            return True

    return False

# check if text contains any of list strs
def contain5(text, list):
    for str in list:
        if _contain5(text, str):
            return True
    return False

# check if text ends with str
def _end5(text, str):

    iter_str = len(str) - 1
    iter_txt = len(text) - 1

    while iter_str >= 0 and iter_txt >=0:
        if text[iter_txt] != str[iter_str]:
            return False
        iter_str -= 1
        iter_txt -= 1
    
    return True

# check if text ends with any of list strs    
def end5(text, list):
    for str in list:
        if _end5(text, str):
            return True
    return False

# check if text is str
def _i5(text, str):
    
    iter_str = 0
    len_str = len(str)

    for ch in text:
        if ch != str[iter_str]:
            return False
        iter_str += 1
        if iter_str == len_str:
            return True

    if iter_str != len_str:
        return False
    
    return True

# check if text is any of list strs    
def i5(text, list):
    for str in list:
        if _i5(text, str):
            return True
    return False

# choose answer from the list
def choo5e(list):
    return list[random.randint( 0, len(list)-1 )]

# check if text ends with any of list strs    
def endswith_list(text, list):
    for str in list:
        if text.endswith(str):
            return True
    return False

# check if text starts with any of list strs    
def startswith_list(text, list):
    for str in list:
        if text.startswith(str):
            return True
    return False


layoutDic = {

    # en2ru
    'q': '??',
    'w': '??',
    'e': '??',
    'r': '??',
    't': '??',
    'y': '??',
    'u': '??',
    'i': '??',
    'o': '??',
    'p': '??',
    '[': '??',
    ']': '??',
    'a': '??',
    's': '??',
    'd': '??',
    'f': '??',
    'g': '??',
    'h': '??',
    'j': '??',
    'k': '??',
    'l': '??',
    ';': '??',
    '\'': '??',
    'z': '??',
    'x': '??',
    'c': '??',
    'v': '??',
    'b': '??',
    'n': '??',
    'm': '??',
    ',': '??',
    '.': '??',
    '/': '.',
    '`': '??',
    '@': '"',
    '#': '???',
    '$': ';',
    '^': ':',
    '&': '?',
    '|': '/',

    # ru2en
    '??': 'q',
    '??': 'w',
    '??': 'e',
    '??': 'r',
    '??': 't',
    '??': 'y',
    '??': 'u',
    '??': 'i',
    '??': 'o',
    '??': 'p',
    '??': '[',
    '??': ']',
    '??': 'a',
    '??': 's',
    '??': 'd',
    '??': 'f',
    '??': 'g',
    '??': 'h',
    '??': 'j',
    '??': 'k',
    '??': 'l',
    '??': ';',
    '??': '\'',
    '??': 'z',
    '??': 'x',
    '??': 'c',
    '??': 'v',
    '??': 'b',
    '??': 'n',
    '??': 'm',
    '??': ',',
    '??': '.',
    #'.': '/',
    '??': '`',
    '"': '@',
    '???': '#',
    #';': '$',
    ':': '^',
    '?': '&',
    '/': '|'
}

# replace incorrect keyboard layout
def replace_layout(text):
    text1 = ''
    for c in text:
        if c in layoutDic:
            text1 += layoutDic[c]
        else:
            text1 += c
    return text1



def dicklist_search(list, key, value):
    for i in range(len(list)):
        if key in list[i]:
            if list[i][key] == value:
                return i
    return -1
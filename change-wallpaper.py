import ctypes

img = "C:/Users/chuu/Documents/GitHub/very-good-fanfiction/THEimage.jpg"

def automaticChange():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img, 0)

automaticChange()
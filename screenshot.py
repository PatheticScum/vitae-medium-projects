# pip install Pillow
# pip install pyscreenshot

import pyscreenshot

img = pyscreenshot.grab()

img.show()
img.save('my_img.png')

from PIL import Image

im = Image.open('gradient.jpg') 
print(f"format: {im.format} \nsize: {im.size} \nmode: {im.mode}")

# converting files to PNG

import os, sys
from PIL import Image

for infile in sys.argv[1:]:
  f, e = os.path.splitext(infile)
  outfile = f + ".png"
  if infile != outfile:
    try:
      with Image.open(infile) as im:
        im.save(outfile)
    except OSError:
      print("cannot convert", infile)
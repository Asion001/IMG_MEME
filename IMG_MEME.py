from PIL import Image, ImageDraw
im = Image.open("archimed.jpg") 
print(im.format, im.size, im.mode)
OUT = []
text = input("Text - ").lower()
outtext = input("Out text - ").lower()
part = im.size[1] // len(text)
region = []
for num in range(len(outtext)):
    OUT.append(text.index(outtext[num]))
for partnum in OUT:  
    box = (0, partnum * part, im.size[0], part + (partnum * part))
    region.append(im.crop(box))
OUTIMG = img = Image.new('RGBA', (im.size[0] , part * len(region)), 'white')
for num in range(len(region)):
    OUTIMG.paste(region[num],(0 , region[num].size[1] * num))
OUTIMG.show()
OUTIMG.save("OUT.png","png")

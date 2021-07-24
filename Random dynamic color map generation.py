from PIL import Image, ImageDraw, ImageFont
import random

color = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
)

ccolor = (
    max(color) + min(color) - color[0],
    max(color) + min(color) - color[1],
    max(color) + min(color) - color[2]
)

FZDBSJWFont = ImageFont.truetype('FZDBSJW.TTF', 180)
iml = Image.new('RGB', (300, 300), color)
imr = Image.new('RGB', (300, 300), ccolor)

frames = []

img = Image.new('RGB', (600, 300))
img.paste(imr, (300, 0))
img.paste(iml, (0, 0))
text = ImageDraw.Draw(img)
text.text((60, 55), "色", font=FZDBSJWFont, fill=ccolor)
text.text((365, 55), "图", font=FZDBSJWFont, fill=color)
frames.append(img)

img = Image.new('RGB', (600, 300))
img.paste(iml, (300, 0))
img.paste(imr, (0, 0))
text = ImageDraw.Draw(img)
text.text((60, 55), "色", font=FZDBSJWFont, fill=color)
text.text((365, 55), "图", font=FZDBSJWFont, fill=ccolor)
frames.append(img)

frames[0].save("test.gif", format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)   
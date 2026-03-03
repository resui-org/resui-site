from PIL import Image

for name in ['RESUI-dark.png', 'RESUI-light.png']:
    img = Image.open(name).convert('RGBA')
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        img.save(name)
        print(f'{name}: cropped to {img.size}')
from PIL import Image, ImageDraw

with open('pi.txt') as f:
    pi_num = str(f.read())[:1000000]

colors = {0: (0, 200, 0), 1: (0, 180, 0), 2: (0, 160, 0), 3: (0, 140, 0), 4: (0, 120, 0),
          5: (0, 100, 0), 6: (0, 80, 0), 7: (0, 60, 0), 8: (0, 40, 0), 9: (0, 20, 0)}


img = Image.new('RGB', (1000, 1000), 'black')
idraw = ImageDraw.Draw(img)
count = 0


for h in range(1000):
    for w in range(1000):
        idraw.rectangle((w, h, w+1, h+1), fill=colors[int(pi_num[count])])
        count += 1


img.save('image/pi_img.jpg')

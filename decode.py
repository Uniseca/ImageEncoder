from PIL import Image
def decode(im):
    width,height = im.size
    lst = []
    times = 0
    for y in range(height):
        for x in range(width):
            r,g,b = im.getpixel((x,y))
            if r|g|b == 0:
                break
            if times%3 == 0:
                index = (g << 8) + b
            elif times%3 == 1:
                index = (r << 8) + g
            else:
                index = (r << 8) + b
            lst.append(chr(index))
            times+=1
    return ''.join(lst)

if __name__ == "__main__":
    dxt = decode(Image.open("encodedImg.bmp","r"))
    with open("decodedTxt.txt","w",encoding="UTF-8") as f:
        f.write(dxt)
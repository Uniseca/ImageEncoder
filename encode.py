from PIL import Image
import math
def encode(txt):
    str_len = len(txt)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB",(width, width),0x0)

    x,y = 0,0
    times = 0
    for i in txt:
        index = ord(i)
        if times%3 == 0:
            rgb = (255, (index & 0xFF00)>>8,index & 0xFF)
        elif times%3 == 1:
            rgb = ((index & 0xFF00)>>8,index & 0xFF ,255)
        else:
            rgb = ((index & 0xFF00)>>8,255,index & 0xFF)
        im.putpixel((x,y),rgb)
        if x == width -1:
            x=0 
            y+=1
        else:
            x+=1
        times+=1
    return im;

if __name__ == "__main__":
    with open("ct.txt",encoding="UTF-8 ") as f:
        dataInText = f.read()
    im = encode(dataInText)
    im.save("encodedImg.bmp")
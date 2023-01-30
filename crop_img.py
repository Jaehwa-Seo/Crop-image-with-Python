import sys
from PIL import Image
import math
####################################################

split_nb = 4

def split_img():
    file_type = ["kor","eng"]

    for num in range(0,2):

        ####################################################
        # crop desktop version
        # 1. Ready kor.png, eng.png in same folder
        # 2. Run 'python crop_img.py'
        #  * If not working, increase image size 
        
        original_img = Image.open("./" + file_type[num] + ".png")
        original_width, original_height = original_img.size

        startx=1000
        starty=1000
        endx=0
        endy=0
        
        for posx in range(0,original_width):
            for posy in range(0,original_height):
                pix_val = original_img.getpixel((posx, posy))
                if((44,85,141,255) == pix_val):
                    if(startx>=posx and starty>=posy):
                        startx = posx
                        starty = posy
                    if(endx<=posx):
                        endx = posx
                    if(endy<=posy):
                        endy = posy

        width = endx - startx + 1
        height = endy - starty + 1

        img  = Image.new( mode = "RGBA", size = (width, height), color = (255, 255, 255, 255) )

        for i in range(0, width):
            for j in range(0, height):
                x_value = startx + i
                y_value = starty + j
                pix_val = original_img.getpixel((x_value, y_value))
                img.putpixel((i,j), pix_val )

        img.save("./codingfamily_1page_" + file_type[num] + ".png")

        ####################################################
        # make mobile version
        a = []
        delay = 0

        for posx in range(4,width):
            if delay == 0:
                pix_val = img.getpixel((posx, 5))
                if((44,85,141,255) == pix_val):
                    a.append(posx)
                    delay = 4
            else:
                delay = delay - 1
        
        a[2] = a[2] -1

        mobile_width = a[0]+4
        mobile_height = height * 4 - 12

        mobile_img = Image.new( mode = "RGBA", size = (mobile_width, mobile_height), color = (255, 255, 255, 255))

        mobile_posx=0
        mobile_posy=0
        for posx in range(0,(a[0]+4)):
            for posy in range(0,height):
                pix_val = img.getpixel((posx, posy))
                mobile_img.putpixel((mobile_posx,mobile_posy), pix_val)
                mobile_posy += 1
            mobile_posy = 0
            mobile_posx += 1
        
        index=0

        for index in range(0,3):
            mobile_posx = 0
            for posx in range(a[index],(a[index+1]+4)):
                mobile_posy = height * (index+1) - (index * 4)
                for posy in range(4,height):
                    pix_val = img.getpixel((posx, posy))
                    mobile_img.putpixel((mobile_posx,mobile_posy), pix_val)
                    mobile_posy += 1
                mobile_posx += 1
            if index == 1:
                a[2] = a[2] + 1

        mobile_img_crop = Image.new( mode = "RGBA", size = (mobile_width-1, mobile_height), color = (255, 255, 255, 255))

        for posx in range(0,mobile_width-1):
            for posy in range(0,mobile_height):
                pix_val = mobile_img.getpixel((posx, posy))
                mobile_img_crop.putpixel((posx,posy), pix_val)
        
        mobile_img_crop.save("./codingfamily_1page_" + file_type[num] + "_mobile.png")
    
split_img()




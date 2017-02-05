#2017-02-03

def getImage(x, y):

    num = "P3 %d %d 255\n"%(x,y)

    j=0
    k=0

    while j < 500:
        while k < 500:

            r = 255;
            g = 255;
            b = 0;
            
            j+=1
            k+=1

            num += "%d %d %d \n"%(r,g,b)
    num += "\n"

    return num

    
if __name__ == '__main__':
    stuff = open("image.ppm", "w")
    stuff.write(getImage(500,500))
    stuff.close()

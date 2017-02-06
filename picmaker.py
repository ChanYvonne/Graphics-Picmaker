#2017-02-03

def getImage(x, y):

    num = "P3 %d %d 255\n"%(x,y)
    
    for k in range(x):
        for j in range(y):

            if j < 100:
                r = 255
                g = 255
                b = 255
                if k > 600:
                    r = 0
                    g = 0
                    b = 255
            if j >= 100 and j < 200:
                r = 255
                g = 255
                b = 0
                if k > 600:
                    r = 255
                    g = 0
                    b = 255
            if j >= 200 and j < 300:
                r = 0
                g = 255
                b = 255
                if k > 600:
                    r = 255
                    g = 255
                    b = 0
            if j >= 300 and j < 400:
                r = 0
                g = 255
                b = 0
                if k > 600:
                    r = 255
                    g = 0
                    b = 0
            if j >= 400 and j < 500:
                r = 255
                g = 0
                b = 255
                if k > 600:
                    r = 0
                    g = 255
                    b = 255
            if j >= 500 and j < 600:
                r = 255
                g = 0
                b = 0
                if k > 600:
                    r = 0
                    g = 0
                    b = 0
            if j >= 600:
                r = 0
                g = 0
                b = 255
                if k > 600:
                    r = 255
                    g = 255
                    b = 255
                
            num += "%d %d %d \n"%(r,g,b)
    
    return num

#print getImage(500,500)
stuff = open("image.ppm", "w")
stuff.write(getImage(700,700))
stuff.close()

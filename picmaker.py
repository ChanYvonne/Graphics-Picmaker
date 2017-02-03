#2017-02-03

stuff = open("image.ppm", "w")
stuff.write(getImage(500,500))
stuff.close()

def getImage(x, y):

    num = "P3 500 500 255\n"

    r=0
    c=0

    while r < 500:
        while c < 500:

            r+=1
            c+=1

    num += "\n"

    

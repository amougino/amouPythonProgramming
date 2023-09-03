import PIL.Image as Img
import os

def createImg(size):
    img = Img.new('RGB', size)
    return(img)

def saveImg(img, path):
    file = os.path.expanduser(path)
    print(file)
    img.save(file)

def display(img):
    img.show()

def getImg(path):
    file = os.path.expanduser(path)
    img = Img.open(file)
    return(img)

image = getImg("~/Desktop/labyrinths/200_280_b/200_280_b_solution.png")
imageSize = image.size
newImage = createImg((imageSize[0] + 2, imageSize[1] + 2))
for x in range(imageSize[0]):
    for y in range(imageSize[1]):
        newImage.putpixel((x+1,y+1), image.getpixel((x,y)))
for x in [0,imageSize[0]+1]:
    for y in range(imageSize[1] + 2):
        newImage.putpixel((x,y), (0,0,0))
for x in range(imageSize[0] + 2):
    for y in [0,imageSize[1]+1]:
        newImage.putpixel((x,y), (0,0,0))
display(newImage)
saveImg(newImage, "~/Desktop/labyrinths/200_280_b/200_280_b_solution_borders.png")
from PIL import Image as img
import os

def get_image(file_path = ''):
    file = os.path.expanduser(file_path)
    if file == '':
        raise(Exception('File not defined'))
    try:
        image = img.open(file)
        return(image)
    except FileNotFoundError:
        raise(Exception('File does not exist'))
    
def create_img(size):
    created_image = img.new('RGB', size, 'white')
    return(created_image)

def save_img(image_to_save, path):
    file = os.path.expanduser(path)
    image_to_save.save(file)

saturn_img = get_image('/Users/amou/Desktop/_1013095.JPG')
saturn_img_size = saturn_img.size

new_image = create_img(saturn_img_size)
print(saturn_img_size)

mult = (5,5,5)
distance = 0
divide = (2*distance + 1)**2

for x in range(saturn_img_size[0]):
    for y in range(saturn_img_size[1]):
        if x > distance - 1 and x < saturn_img_size[0] - distance and y > distance - 1 and y < saturn_img_size[1] - distance:
            sum_around = [0,0,0]
            for i in range(-distance,distance+1):
                for j in range(-distance,distance+1):
                    pixel = saturn_img.getpixel((x+i,y+j))
                    for idx,color in enumerate(pixel):
                        sum_around[idx] += color
            new_image.putpixel((x,y),(int(sum_around[0]*mult[0]/divide),int(sum_around[1]*mult[1]/divide),int(sum_around[2]*mult[2]/divide)))
        else:
            new_image.putpixel((x,y),(0,0,255))

    print(x)

save_img(new_image,'/Users/amou/Desktop/saturn_bright_2_blur1_m15.png')
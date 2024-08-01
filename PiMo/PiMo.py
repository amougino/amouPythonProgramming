import os
import PIL.Image as img

#all possible characters for strings (here the first object has a value of 1 and the last a value of 254)
chars = [' ', '!', '“', '"', '#', '$', '%', '&', '‘', "'", '(', ')', '*', '+', ',', '-', 
         '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', 
         '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', 
         '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', 
         '~', '÷', '¡', '¢', '£', '€', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', 
         '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¿', 'À', 'Á',
         'Ã', 'Ä', 'Å', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 
         'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 
         'ä', 'å', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 
         'õ', 'ö', 'Б', 'Г', 'Д', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'П', 'У', 'Ф', 'Ц', 'Ч', 
         'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'б', 'в', 'г', 'д', 'ж', 'з', 'и', 'й', 
         'к', 'л', 'м', 'н', 'п', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 
         'ю', 'я', 'Δ', 'Θ', 'Λ', 'Ξ', 'Π', 'Σ', 'Φ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 
         'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω']

colors = {
    'black':    (0,0,0),
    'white':    (255,255,255),
    'red':      (255,0,0),
    'green':    (0,255,0),
    'blue':     (0,0,255),
    'magenta':  (255,0,255),
    'yellow':   (255,255,0),
    'cyan':     (0,255,255),
    'd_red':    (128,0,0),
    'd_green':  (0,128,0),
    'd_blue':   (0,0,128),
    'orange':   (255,128,0),
    'lime':     (128,255,0),
    'apple':    (0,255,128),
    'azure':    (0,128,255),
    'indigo':   (128,0,255),
    'pink':     (255,0,128),
    'l_magenta':(255,128,255),
    'l_yellow': (255,255,128),
    'l_cyan':   (128,255,255)
}

def get_image(file_path = ''):
    file = os.path.expanduser(file_path)
    if file == '':
        raise(Exception('File not defined'))
    try:
        image = img.open(file)
        return(image)
    except FileNotFoundError:
        raise(Exception('File does not exist'))
    


class cursor:

    def __init__(self, image, starting_pos = (0,0), direction = [1,0]):
        self.image = image
        self.imageSize = image.size
        self.pos = starting_pos
        self.direction = direction
        self.active = True
        self.processes = {
            (255,0,0):self.end_program
        }

    def cell_valid_movement(self,cell):
        valid = True
        try:
            if self.image.getpixel(cell) == colors['black']:
                valid = False
        except IndexError:
            valid = False
        for xy in range(2):
            if cell[xy] < 0:
                valid = False
        return(valid)

    def check_for_walls(self):
        count = 0
        while self.cell_valid_movement((
            self.pos[0] + self.direction[0],
            self.pos[1] + self.direction[1]
            )) == False:
            count += 1
            if count >= 4:
                raise Exception('ERROR : Cursor stuck in walls')
            if self.direction[1] != 0:
                self.direction[0] = self.direction[1]*(-1)
                self.direction[1] = 0
            else:
                self.direction[1] = self.direction[0]
                self.direction[0] = 0
            
    def end_program(self):
        self.active = False

    def evaluate_cell(self):
        try:
            self.processes[self.image.getpixel(self.pos)]
        except KeyError:
            print('ignored (to remove later)')

    def move(self):
        self.pos = (
            self.pos[0] + self.direction[0],
            self.pos[1] + self.direction[1]
            )

    def read_cell(self):
        pass

if __name__ == '__main__':
    cursor = cursor(get_image(os.getcwd()+'/PiMo/PiMoImage2.png'))
    moves = 0
    print('startpos',cursor.pos)
    while moves < 10:
        cursor.evaluate_cell()
        cursor.check_for_walls()
        cursor.move()
        print('pos',cursor.pos)
        moves += 1
        if cursor.active == False:
            print('program ended')
            break
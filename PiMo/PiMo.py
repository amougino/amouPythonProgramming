import os
import PIL.Image as img
import operator

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
         'ζ', 'η', 'θ', 'λ', 'μ', 'ν', 'ξ', 'π', 'ρ', 'ς', 'σ', 'φ', 'ψ', 'ω', '∈']

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

comparators_processes = {
    '==':operator.eq,
    '!=':operator.ne,
    '>':operator.gt,
    '<':operator.lt,
    '>=':operator.ge,
    '<=':operator.le
}

comparators = []
for comparator in comparators_processes:
    comparators.append(comparator)

operations_processes = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv,
    '%':operator.mod,
    '//':operator.floordiv,
    '**':operator.pow
}

operations = []
for operation in operations_processes:
    operations.append(operation)

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
        self.image_size = image.size
        self.pos = starting_pos
        self.direction = direction

        self.active = True

        self.processes = {
            colors['black']:self.error_in_wall,
            colors['red']:self.end_program,
            colors['blue']:self.store_in_cell,
            colors['magenta']:self.go_to,
            colors['yellow']:self.turn_right,
            colors['cyan']:self.remove_from_stack,
            colors['d_red']:self.get_input,
            colors['d_green']:self.print_cell,
            colors['d_blue']:self.ignore_pixels,
            colors['orange']:self.int_to_stack,
            colors['lime']:self.str_to_stack,
            colors['apple']:self.copy_cell,
            colors['pink']:self.duplicate_stack_top
        }
        self.stack = []
        self.small_stack_str = ''
        self.small_stack_oper = ''
        self.small_stack_comp = ''
        self.expecting = ('all',0)
        self.movement = True
        self.cells = {}
        '''
        + #white : ignore
        + #black : wall
        + #red : end program
        @green : condition (cell,comparator,cell)
        + @blue : store (cell int,value)
        + @magenta : goto (int,int)
        + @yellow : turn (int)
        + @cyan : remove from stack (amount to remove is int on top of stack and is not counted in the args removed)
        + @d_red : get input (cell) -> how does it know if string or int??? -> maybe an int can start with a # ?
        + @d_green : print (cell)                                                                                                                                                                                                                                                                                                                                 
        + @d_blue : ignore next cells (int)
        + @%orange : add cell/int value to stack (if int on stack, can be used to add larger numbers / multiple numbers (idk yet))
        + @%lime : add str value to stack (if int on stack, can be used to add multiple chars. each pixel can hold up to 3 chars, no chars is 255 -> example : to add 11 do (19,19,255))
        + @apple : copy (cell,cell) doesnt do anything if cell to copy isnt filled
        @azure : operation (add,sub,mult,div) (type(0,1,2,3,4...),cell1,cell2,cell3... if unused cell in stack -> it will be used to store result -> otherwise will use the first cell used)
        - @%indigo : comparator (equal,greater,less,>=,<=... needs int)
        + @pink : duplicate top of stack
        &l_magenta : free slot for func?
        &l_yellow : free slot for func?
        &l_cyan : free slot for func?

        #  special
        @  function that accesses and uses args on stack
        @% ( (uses arg(s) and then ) adds to stack
        &  user can add their own functions

        to do list
         - azure
         - indigo / green
        '''

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
                raise Exception('ERROR : Cursor surrounded by walls')
            self.turn_right()
            
    def error_in_wall(self):
        raise Exception('ERROR : Cursor in wall')

    def end_program(self):
        self.active = False

    def store_in_cell(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-1], int):
                if isinstance(self.stack[-2], int) or isinstance(self.stack[-2], str):
                    self.cells[self.stack[-1]] = self.stack[-2]
                    self.stack = self.stack[:-2]
            else:
                raise Exception('ERROR : Argument not an integer, no cell to store in')
        else:
            raise Exception('ERROR : Insufficient arguments in stack to store in cell')

    def go_to(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-2], int):
                if isinstance(self.stack[-1], int):
                    if self.cell_valid_movement((self.stack[-2],self.stack[-1])):
                        self.pos = (self.stack[-2],self.stack[-1])
                        self.stack = self.stack[:-2]
                        self.movement = False
                    else:
                        raise Exception('ERROR : Cannot go to cell, not a valid movement')
                else:
                    raise Exception('ERROR : Second value for movement not an integer')
            else:
                raise Exception('ERROR : First value for movement not an integer')
        else:
            raise Exception('ERROR : Insufficient arguments for movement')

    def turn_right(self):
        if self.direction[1] != 0:
            self.direction[0] = self.direction[1]*-1
            self.direction[1] = 0
        else:
            self.direction[1] = self.direction[0]
            self.direction[0] = 0

    def remove_from_stack(self):
        if len(self.stack) > 0:
            self.stack.pop(-1)
        else:
            print('nothing to remove (to remove later)') ###

    def get_input(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                if self.stack[-1] > 0:
                    input_value = input(f'INPUT - at cell {self.pos} - ')
                    if input_value[0] == '#':
                        self.cells[self.stack[-1]] = int(input_value[1:])
                    else:
                        self.cells[self.stack[-1]] = input_value
                    self.stack.pop(-1)
                else:
                    raise Exception('ERROR : Cell key as input cannot be negative')
            else:
                raise Exception('ERROR : Argument not an integer, no cell indicated to input to')
        else:
            raise Exception('ERROR : Insufficient arguments to input')

    def print_cell(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                if self.stack[-1] > 0:
                    print('pimo >>>',self.cells[self.stack[-1]])
                    self.stack.pop(-1)
                else:
                    raise Exception('ERROR : Cell key to print cannot be negative')
            else:
                raise Exception('ERROR : Argument not an integer, no cell indicated to be printed')
        else:
            raise Exception('ERROR : Insufficient arguments to print')
        
    def ignore_pixels(self):
        if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                if self.stack[-1] > 0:
                    self.expecting = ('pass',self.stack[-1])
                    self.stack.pop(-1)
                else:
                    self.expecting = ('pass',1)
            else:
                self.expecting = ('pass',1)
        else:
            self.expecting = ('pass',1)

    def int_to_stack(self):
        '''if len(self.stack) >= 1:
            if isinstance(self.stack[-1], int):
                if self.stack[-1] > 0:
                    self.expecting = ('int',self.stack[-1])
                    self.stack.pop(-1)
                else:
                    self.expecting = ('int',1)
            else:
                self.expecting = ('int',1)
        else:
            self.expecting = ('int',1)'''
        self.expecting = ('int',1)
    
    def str_to_stack(self):
        if self.expecting[0] == 'all':
            if len(self.stack) > 0:
                if isinstance(self.stack[-1], int):
                    if self.stack[-1] > 0:
                        self.expecting = ('str',self.stack[-1])
                        self.stack.pop(-1)
                    else:
                        self.expecting = ('str',1)
                else:
                    self.expecting = ('str',1)
            else:
                self.expecting = ('str',1)
        else:
            raise Exception('ERROR : Unexpected value (str_to_stack)')
        
    def copy_cell(self):
        if len(self.stack) >= 2:
            if isinstance(self.stack[-2], int):
                if isinstance(self.stack[-1], int):
                    try:
                        self.cells[self.stack[-1]] = self.cells[self.stack[-2]]
                    except KeyError:
                        raise Exception('ERROR : Cell to copy does not exist')
                    self.stack = self.stack[:-2]
                else:
                    raise Exception('ERROR : Second argument not an integer, no cell to copy to')
            else:
                raise Exception('ERROR : First argument not an integer, no cell to be copied')
        else:
            raise Exception('ERROR : Insufficient arguments to copy')
        
    def operation_to_stack(self):
        self.expecting = ('oper',1)

    def duplicate_stack_top(self):
        if len(self.stack) > 0:
            self.stack.append(self.stack[-1])
        else:
            raise Exception('ERROR : No arguments to duplicate')

    def evaluate_cell(self):
        if self.expecting[0] == 'all':
            try:
                self.processes[self.image.getpixel(self.pos)]()
            except KeyError:
                #print('ignored (to remove later)') ###
                pass

        elif self.expecting[0] == 'int':
            current_pixel = self.image.getpixel(self.pos)
            if current_pixel != colors['white']:
                self.stack.append(
                    (255 - current_pixel[2]) +
                    (255 - current_pixel[1]) * 256 +
                    (255 - current_pixel[0]) * (256**2)
                    )
                self.expecting = ('int',self.expecting[1] - 1)
                if self.expecting[1] <= 0:
                    self.expecting = ('all',0)

        elif self.expecting[0] == 'str':
            current_pixel = self.image.getpixel(self.pos)
            if current_pixel != colors['white']:
                for value in current_pixel:
                    if value != 255:
                        self.small_stack_str += chars[value]
                self.expecting = ('str',self.expecting[1] - 1)
                if self.expecting[1] <= 0:
                    self.expecting = ('all',0)
                    self.stack.append(self.small_stack_str)
                    self.small_stack_str = ''

        elif self.expecting[0] == 'pass':
            current_pixel = self.image.getpixel(self.pos)
            if current_pixel != colors['white']:
                self.expecting = ('pass',self.expecting[1] - 1)
                if self.expecting[1] <= 0:
                    self.expecting = ('all',0)

        elif self.expecting[0] == 'oper':
            current_pixel = self.image.getpixel(self.pos)
            if current_pixel != colors['white']:
                for value in current_pixel:
                    if value != 255:
                        self.small_stack_oper += operations[value%len(operations)]
                self.expecting = ('oper',self.expecting[1] - 1)
                if self.expecting[1] <= 0:
                    self.expecting = ('all',0)

    def operate(self):
        pass

    def move(self):
        if self.movement:
            self.pos = (
                self.pos[0] + self.direction[0],
                self.pos[1] + self.direction[1]
                )
        else:
            self.movement = True

if __name__ == '__main__':
    cursor = cursor(get_image(os.getcwd()+'/PiMo/PiMoImage7.png'))
    moves = 0 ###
    #print('startpos',cursor.pos) ###
    while moves < 40:
        cursor.evaluate_cell()
        if cursor.active == False:
            print('end program',cursor.stack)
            break
        cursor.check_for_walls()
        cursor.move()
        print(
            'pos',cursor.pos,
            'stack',cursor.stack,
            'expecting',cursor.expecting,
            'cells',cursor.cells,
            'color',cursor.image.getpixel(cursor.pos)
            ) ###
        moves += 1
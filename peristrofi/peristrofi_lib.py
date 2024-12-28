# rotation
import os

def open_file():
    pass

def analyse_file():
    pass

def file_to_vel_pos():
    pass

class Num:

    def __init__(self,value,power,precision):
        self.val = value
        self.pow = power
        self.prec = precision
        self.change_prec_round(precision)

    def change_prec_round(self,new_prec):
        if new_prec > self.pow:
            delta_pow = 10 ** (new_prec - self.pow)
            new_val = self.val // delta_pow
            if self.val % delta_pow >= delta_pow / 2:
                new_val += 1
            self.val = new_val
            self.pow = new_prec

    def change_prec_no_round(self,new_prec):
        if new_prec > self.pow:
            delta_pow = 10 ** (new_prec - self.pow)
            self.val = self.val // delta_pow
            self.pow = new_prec

    def __add__(self,other):
        if other.pow > self.pow:
            delta_pow = 10 ** (other.pow - self.pow)
            self.val += other.val * delta_pow
        else:
            delta_pow = 10 ** (self.pow - other.pow)
            self.val = self.val * delta_pow + other.val
            self.pow = other.pow
        self.change_prec_round(self.prec)
        return(self)

    def __mul__(self,other):
        self.val *= other.val
        self.pow += other.pow
        self.change_prec_round(self.prec)
        return(self)

    def __div__(self,other):
        pass

class MagNum:
    
    def __init__(self,float_val = 0,prec = -8):
        if float_val < 0:
            self.sign = -1
            float_val = -float_val
        else:
            self.sign = 1
        split_float = str(float_val).split('.')
        if len(split_float) == 2 and split_float[1] != '0':
            self.val = [int(char) for char in split_float[0] + split_float[1]]
            self.pow = -len(split_float[1])
        else:
            self.pow = 0
            while split_float[0][-1] == '0':
                self.pow += 1
                split_float[0] = split_float[0][:-1]
            self.val = [int(char) for char in split_float[0]]
        self.change_prec_no_round(prec)

    def change_prec_round(self,new_prec):
        if new_prec > self.pow:
            new_val = self.val[:self.pow-new_prec]
            if self.val[self.pow-new_prec] >= 5:
                new_val[-1] += 1
            self.val = new_val
            self.pow = new_prec

    def change_prec_no_round(self,new_prec):
        if new_prec > self.pow:
            self.val = self.val[:self.pow-new_prec]
            self.pow = new_prec

    def flatten(self):
        for i in range(1,len(self.val)):
            idx = len(self.val) - i
            self.val[idx - 1] += self.val[idx] // 10
            self.val[idx] %= 10
        while self.val[0] // 10 != 0:
            self.val.insert(0, self.val[0] // 10)
            self.val[1] %= 10
            
    def __add__(self,other):
        if other.pow > self.pow:
            other.val += [0 for i in range(other.pow - self.pow)]
        else:
            self.val += [0 for i in range(self.pow - other.pow)]
            self.pow = other.pow
        len_self = len(self.val)
        len_other = len(other.val)
        if len_self > len_other:
            other.val = [0 for i in range(len_self - len_other)] + other.val
        else:
            self.val = [0 for i in range(len_other - len_self)] + self.val
        for i in range(len(self.val)):
            self.val[i] += other.val[i]
        self.flatten()
        return(self)

class Vector:
    pass

class Body:
    pass

class System:
    pass
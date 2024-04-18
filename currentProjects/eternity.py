'''
Notes

Class:
    val = []
    decimal pos = (int)


    func
        add
        sub
        mult
        divi
        op
        adjust (add 0s to beginning / end)
        embellish (remove 0s)
        

'''

class Eternal:

    def __init__(self, val, sign, base = 10, baseList = None, decChar = '.'):
        
        self.val = val
        self.sign = sign
        self.decChar = decChar
        
        if baseList == None:
            if base <= 10:
                self.base = [str(digit) for digit in range(base)]
            else:
                raise Exception('ERROR - Define baseList to use higher bases than 10')
        else:
            self.base = baseList
        
        for char in self.val:
            if not char in self.base:
                if char != decChar:
                    raise Exception('ERROR - Character(s) not in base')
        
        decCharFound = 0
        for char in self.val:
            if char == decChar:
                decCharFound += 1
        if decCharFound > 1:
            raise Exception('ERROR - Too many decimal characters')
        elif decCharFound == 0:
            self.val.append(decChar)
            self.val.append(self.base[0])
            
        self.fold()
        
    def __str__(self):
      
        strVal = ''.join(self.val)
        return(strVal)
        
    def convert(self, base):

        pass
        
    def fold(self):
        
        while self.val[0] == self.base[0]:
            if self.val[1] == self.decChar:
                break
            else:
                self.val.pop(0)
        while self.val[-1] == self.base[0]:
            if self.val[-2] == self.decChar:
                break
            else:
                self.val.pop(-1)
    
    def unfold(self, other):
    
        if self.base == other.base:
            preDec = self.val.index(self.decChar) - other.val.index(other.decChar)
            if preDec < 0:
                for i in range(preDec * -1):
                    self.val.insert(0, self.base[0])
            postDec = (len(self.val) - self.val.index(self.decChar) - 1) - (len(other.val) - other.val.index(other.decChar) - 1)
            if postDec < 0:
                for i in range(postDec * -1):
                    self.val.append(self.base[0])
        else:
            raise Exception('ERROR - Cannot unfold as Eternals not in same base')
            
        
        
        
a = Eternal(['0', '6', '.', '5'], '+', base = 10)
#a.fold()
#a.unfold(Eternal(['0', '0', '1', '.', '1', '0'], '+', base = 10))
#a.fold()
print(a)
'''
1 1 . 1
0 1 2 3
'''

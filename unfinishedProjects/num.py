class num:
    
    def __init__(self, val, sign = True, base = 10):

        self.sign = sign
        self.base = base

        if isinstance(val, int):
            self.value = [char for char in str(val)]
            
        if isinstance(val, float):
            self.value = [char for char in str(val)]

        if isinstance(val, list):
            self.value = val
        
        for i in range(len(self.value)):
            if self.value[i] != '.':
                self.value[i] = int(self.value[i])
        if self.value[0] == '.':
            self.value.insert(0, 0)
        if self.value[-1] == '.':
            self.value.append(0)
        try: 
            preDec = self.value.index('.')
        except ValueError:
            self.value.append('.')
            self.value.append(0)
        
    def findDecimal(self):
        return(self.value.index('.'))
    
    def flatten(self):
        for i in range(len(self.value)):
            obj = len(self.value) - i - 1
            if self.value[obj] != '.':
                if self.value[obj] >= self.base:
                    self.value[obj] -= self.base
                    if self.value[obj - 1] == '.':
                        self.value[obj - 2] += 1
                    elif obj == 0:
                        self.value.insert(0, 1)
                    else:
                        self.value[obj - 1] += 1
    
    def operation(self, op, num):
        if op == 'add':
            if self.sign == True:
                if num.sign == True:
                    self.add(num)
                else:
                    self.sub(num)
            else:
                if num.sign == True:
                    self.sub(num)
                else:
                    self.add(num)
        if op == 'sub':
            if self.sign == True:
                if num.sign == True:
                    self.sub(num)
                else:
                    self.add(num)
            else:
                if num.sign == True:
                    self.add(num)
                else:
                    self.sub(num)
    
    def add(self, num):
        preDec = self.findDecimal()
        preDec2 = num.findDecimal()

        if preDec < preDec2:
            while preDec < preDec2:
                self.value.insert(0, 0)
                preDec = self.findDecimal()
                
        for i in range(preDec):
            if preDec2 - i - 1 >= 0:
                self.value[preDec - i - 1] += num.value[preDec2 - i - 1]
                
        postDec = len(self.value) - preDec - 1
        postDec2 = len(num.value) - preDec2 - 1
        
        if postDec < postDec2:
            while postDec < postDec2:
                self.value.append(0)
                postDec = len(self.value) - preDec - 1
                
        for i in range(postDec):
            if preDec2 + i + 1 <= len(num.value) - 1:
                self.value[preDec + i + 1] += num.value[preDec2 + i + 1]
                
        self.flatten()
        
    def sub(self, num):
        preDec = self.findDecimal()
        preDec2 = num.findDecimal()

        if preDec < preDec2:
            while preDec < preDec2:
                self.value.insert(0, 0)
                preDec = self.findDecimal()

        postDec = len(self.value) - preDec - 1
        postDec2 = len(num.value) - preDec2 - 1
        
        if postDec < postDec2:
            while postDec < postDec2:
                self.value.append(0)
                postDec = len(self.value) - preDec - 1

        for i in range(postDec):
            if postDec - i <= postDec2:
                if self.value[-i] >= num.value[-i]:
                    self.value[-i] -= num.value[-i]
                else:
                    carryFound = False
                    searchDigit = i + 1
                    while carryFound == False:
                        if searchDigit <= len(self.value) - 1:
                            if self.value[-searchDigit] == '.':
                                searchDigit += 1
                            else:
                                if self.value[-searchDigit] != 0:
                                    pass #remove 1 for here, add base -1 to all until -i, add 10 to -i, do subtraction
                                else:
                                    searchDigit += 1
                        else:
                            pass #num - self.value and self.sign = opposite

                    
                
    def printVal(self):
        print(self.value)
        
    
        
a = num(0.0123456)
b = num(0.0123456)
a.operation('add', b)
a.printVal()
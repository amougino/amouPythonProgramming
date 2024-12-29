from peristrofi_lib import *

settings = [
    {
        'mass_unit' : 'kg',
        'mass_prec' : -8
    }
]

if __name__ == '__main__':
    vala = 10.0000015
    valb = 3.1414
    a = MagNum(vala,-6)
    b = MagNum(valb,-6)
    c = a + b
    print(a,b,c,vala + valb)

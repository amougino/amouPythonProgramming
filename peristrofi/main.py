from peristrofi_lib import *

settings = [
    {
        'mass_unit' : 'kg',
        'mass_prec' : -8
    }
]

if __name__ == '__main__':
    a = MagNum(1000)
    b = MagNum(1000)
    a -= b
    print(a)

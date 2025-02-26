from peristrofi_lib import *
import random

settings = [
    {
        'mass_unit' : 'kg',
        'mass_prec' : -8
    }
]

if __name__ == '__main__':
    a = MagNum(1)
    a -= MagNum(2)
    print(a)
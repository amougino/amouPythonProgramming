from peristrofi_lib import *

settings = [
    {
        'mass_unit' : 'kg',
        'mass_prec' : -8
    }
]

if __name__ == '__main__':
    a = MagNum(3.141)
    b = MagNum(2.718)
    a += b
    print(a.val,a.pow)

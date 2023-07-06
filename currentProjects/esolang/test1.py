'''
< > / # ! ? _ & ~ . , ; : | [ ]

numbers in base 8 = _ & ~ . , ; : |
    + / = dot

_ 0
& 1
~ 2
. 3
, 4
; 5
: 6
| 7

> without < before = imports

'''

chars = [' ', '!', '"', '#', '%', '&', "'", '(', 
         ')', '*', '+', ',', '-', '.', '/', '0', 
         '1', '2', '3', '4', '5', '6', '7', '8', 
         '9', ':', ';', '<', '=', '>', '?', '@', 
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
         'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
         'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
         'Y', 'Z', '[', '\\', ']', '_', '|', '~']
print(len(chars))

'''

; before text = variable name
# before text = str
_ before text = int / float
/ before text = list
? = list separator
/ = list index
! = close list (if lists in lists)
    example of list defining:
        ;:..,:~:./__!#,|;_
        test[0] = "hi"
        ;:..,:~:./_&!/__?_&?/_~?_.!?_,
        test[1] = [0, 1, [2, 3], 4]
? = if
! = =
<> indicate number of tab
| before text = special func
| takes into account next 2 chars
    so |_~|_~ = **
00 +
01 -
02 *
03 /
len

'''
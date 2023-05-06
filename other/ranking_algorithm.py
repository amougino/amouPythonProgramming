users = 50000 # number of users
likes = 1 # number of likes
time = 4147200 # number of seconds that the post has existed
x = 1000 # changeable value
y = 50000 # changeable value
start = 100 # changeable value esthetics

a = start + ( ( likes / users ) * x )

b = a - ( time / ( ( likes / users ) * y ) )

print( a )
print( b )

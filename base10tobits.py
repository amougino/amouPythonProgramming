num = int(input('Number - '))
bits = 1
while 2**(bits-1) < num:
    bits += 1
answer = []
for i in range(bits):
    if num >= 2**(bits-1-i):
        num -= 2**(bits-1-i)
        answer.append(1)
    else:
        answer.append(0)
if answer[0] == 0:
    answer.pop(0)
print(answer)
# ClemCode
# Made by amou, also known as DrShock, at the request of cbio
# If modifications are needed, please contact the creator
# Please do not copy this code, or claim it as your own
# Please do not pretend to be the creator of this code
# Other than that, enjoy the code!

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

def splitString(string):
    return [char for char in string]

def unSplitString(string):
    response = ''
    for i in string:
        response = response + i
    return(response)

def getMsg():
  valid = False
  while valid == False:
    msg = input('\n'+'Message - ')
    valid = True
    for i in splitString(msg):
      if valid == True:
        if not i in char:
          valid = False
    if valid == False:
      print('\n'+'ERROR - Character(s) not valid')
  return(msg)

def getNum():
  valid = False
  while valid == False:
    num = input('\n'+'Number - ')
    try:
      numInt = int(num)
      valid = True
      if numInt < 0:
        numInt *= -1
        if numInt >= len(char):
          numInt %= len(char)
        numInt = len(char) - numInt
    except ValueError:
      valid = False
      print('\n'+'ERROR - Number(s) not valid')
  return(numInt)

def codeMsg(msg,numInt):
  msgList = splitString(msg)
  if numInt >= len(char):
    numInt %= len(char)
  for idx,i in enumerate(msgList):
    charIdx = char.index(i)
    if charIdx + numInt >= len(char):
      msgList[idx] = char[charIdx + numInt - len(char)]
    else:
      msgList[idx] = char[charIdx + numInt]
  msg = unSplitString(msgList)
  return(msg)

msg = getMsg()
num = getNum()
print('\nOutput between brackets : ['+codeMsg(msg,num) + ']\n')
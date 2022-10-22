charList = ['A', 'B', 'C', 'D', 'E', 'F']
characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','.',',','?','!','(',')','-','+','*','=','<','>','"','/']
numberList = ['44', '44', '44', '44', '44', '44', '44', '44', '01', '48', '47', '46', '45', '44', '43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '49', '00']
def encodeNumber(characterList,settings):
    for i in range(len(settings)):
        settings[i] = int(settings[i])
    for i in range(len(characterList)):
        characterList[i] = characters[settings[i+8]]
    print(characterList)
encodeNumber(charList,numberList)
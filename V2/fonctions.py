def importDic(fileName: str) -> dict:
    file = open(fileName, 'r')
    lignes = file.readlines()
    file.close()
    dico = {} # Création d'un dictionnaire contenant les équivalences
    for ligne in lignes:
        mots = ligne.split(',')
        dico[mots[0]] = mots[1][:-1]
    return dico

def humanToLeet(text: str, dic: dict) -> str:
    text = text.upper()
    newText = ''
    
    for lettre in text:
        if dic.get(lettre) != None:
            newText += dic[lettre]
        else:
            newText += lettre
    return newText

def maxLetters(dico):
    max = 0
    for key in dico:
        if len(dico[key]) > max:
            max = len(dico[key])
    return max

def returnDic(dic):
    return {dic[key]: key for key in dic}

def leetToHuman(text: str, dic: dict) -> str:
    max = maxLetters(dic)
    invDic = returnDic(dic)
    newText = ''
    
    while len(text) > 0:
        cond = True
        for j in range(max, -1, - 1):
            c = text[:j]
            if invDic.get(c) != None:
                newText += invDic[c]
                text = text[j:]
                cond = False
                break
        if cond:
            newText += text[0]
            text = text[1:]
    return newText
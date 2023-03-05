def value(pessoa,key_word):
    if key_word == "Processo":
        return pessoa[0]
    elif key_word == "Ano":
        return pessoa[1][0]
    elif key_word == "Mes":
        return pessoa[1][1]
    elif key_word == "Dia":
        return pessoa[1][2]
    elif key_word == "Nome":
        return pessoa[2]
    elif key_word == "Pai":
        return pessoa[3]
    elif key_word == "Mae":
        return pessoa[4]
    elif key_word == "Observações":
        return pessoa[5]
    elif key_word == "nome propio":
        return pessoa[5]
    elif key_word == "apelido":
        return pessoa[5]
    
def frequencia(pessoas,key_word,tempo):
    frequencias = {}
    for pessoa in pessoas:
        valor = value(pessoa,key_word)
        if (tempo!=0):
            ano_index = value(pessoa,"Ano")//tempo
            if (ano_index in frequencias):
                if( valor in frequencias[ano_index]):
                    frequencias[ano_index][valor]+=1
                else :
                    frequencias[ano_index][valor]=1
            else :
                frequencias[ano_index]={}
                frequencias[ano_index][valor]=1
        else:
            if( valor in frequencias):
                frequencias[valor]+=1
            else :
                frequencias[valor]=1
    return frequencias

def print_tabelas(dict1,dim):

    if dim == 1:
        if type(list(dict1.values())[0]) is dict :
            for key in list(dict1):
                dict1[key]=len(dict1[key])
    
    string = ""

    x = len(dict1)
    y = len(list(dict1.values())[0])

    
    tam_1=0
    keys = sorted(list(dict1.keys()))
    for nome in keys:
        if (len(str(nome))>tam_1):
            tam_1 = len(str(nome))
    tam_1 += 4
    tam_2 = 0
    for valor in dict1.values():
        if (len(str(valor))>tam_1):
            tam_2 = len(str(valor))
    tam_2 += 4

    for i in range(tam_1+tam_2+1):
        string += '-'

    for i in range(len(keys)):
        string += "\n|" + str(keys[i])
        for n in range(len(str(keys[i])), tam_1-1):
            string += ' '
        string += '|' + str(dict1[keys[i]])
        for n in range(len(str(dict1[keys[i]])), tam_2-1):
            string += ' '
        string += "|\n|"
        for i in range(tam_1-1):
            string += '-'
        string += "|"
        for i in range(tam_2-1):
            string += '-'
        string += "|"
    print(string)
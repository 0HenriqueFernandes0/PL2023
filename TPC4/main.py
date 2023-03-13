import re

def json(list_i,path):

    pagjson="["
    for dict in list_i:
        pagjson+="""
            {\n"""

        for i in dict.keys():
            if type(dict[i]) is not list:
                value = dict[i]
                if(not value.isdigit()):
                    value = f""" "{value}" """
                pagjson+=f"""           "{i}":{value},\n"""
            else:
                pagjson+=f"""           "{i}":["""
                for value in dict[i]:
                    if(not value.isdigit()):
                        value = f"""    "{value}" """
                    pagjson+=f"{value},"
                pagjson=pagjson[:-1]
                pagjson+="],\n"

        pagjson=pagjson[:-2]
        pagjson+="""
        },"""

    pagjson=pagjson[:-1]
    pagjson+="""
    ]"""

    file = open(path+".json", "w")
    file.write(pagjson)
    file.close()

def parse(path):
    file = open(path,"r")
    lines = file.read().split('\n')
    
    cabeçalho = re.findall(r"(\w+(?:{\d+}(?:::(?:\w)+)*|{\d+,\d+}(?:::(?:\w)+)*)*)",lines[0])

    expre = ""
    for colun in cabeçalho:
        n = re.search(r"{(\d+)}",colun)
        if (n):
            grupo = colun.split("{")[0]
            for i in range(int(n.group(1))):
                expre+=f"(?P<{grupo}{i}>\w+),"
        else: 
            n = re.search(r"{(\d+),(\d+)}",colun)
            if (n):
                grupo = colun.split("{")[0]
                for i in range(int(n.group(1))):
                    expre+=f"(?P<{grupo}{i}>\w+),"
                for i in range(int(n.group(1)),int(n.group(2))):
                    expre+=f"(?P<{grupo}{i}>\w*),"
            else:
                expre+=f"(?P<{colun}>\w+),"
    expre=expre[:-1]


    lista = []
    for line in lines:
        n = re.match(expre,line)
        if n :
            dict={}
            for i in range(len(cabeçalho)):
                if "{" not in cabeçalho[i]:
                    dict[cabeçalho[i]]=n.group(cabeçalho[i])
                else:
                    grupo = cabeçalho[i].split("{")[0]

                    new_dict = n.groupdict()
                    lista_valores=[new_dict[grupo+"0"]]
                    j=1
                    key = grupo+str(j)
                    while key in new_dict.keys():
                        if new_dict[key] == "":
                            break
                        lista_valores.append(new_dict[key])
                        j+=1
                        key = grupo+str(j)
                    operation = cabeçalho[i].split("::")[1]
                    if operation == "":
                        dict[grupo]=lista_valores
                    elif operation == "sum":
                        lista_valores= list(map(int, lista_valores))
                        dict[grupo] = str(sum(lista_valores))
                    elif operation == "media":
                        lista_valores= list(map(int, lista_valores))
                        dict[grupo] = str(sum(lista_valores)/len(lista_valores))
                    elif operation == "maior":
                        dict[grupo] = str(max(lista_valores, key=int))
                    elif operation == "menor":
                        dict[grupo] = str(min(lista_valores, key=int))
        
            lista.append(dict)

    return lista
    

def main():
    path="myheart.csv"
    set = parse(path)
    json(set,path.split(".")[0])
                


if __name__ == '__main__':
    main()
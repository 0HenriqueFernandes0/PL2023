import re

def json(list):

    pagjson="["
    for dict in list:
        pagjson+="""
            {
                """

        for i in dict.keys():
            if type(dict[i]) != list:
                value = dict[i]
                if(not value.isdigit()):
                    value = f""" "{value}" """
                pagjson+=f"""       "{i}":{value},\n"""
            else:
                pagjson+=+f"""       {i}:["""
                for value in dict[i]:
                    if(not value.isdigit()):
                        value = f""" "{value}" """
                    pagjson+=f"{value},"
                pagjson=pagjson[:-1]
                pagjson+="],"

        pagjson=pagjson[:-2]
        pagjson+="""
        },"""

    pagjson=pagjson[:-1]
    pagjson+="""
    ]"""

    file = open("output.json", "w")
    file.write(pagjson)
    file.close()

def parse(path):
    file = open(path,"r")
    lines = file.read().split('\n')
    
    cabeçalho = re.findall(r"(\w+(?:{\d+}|{\d+,\d+})*)",lines[0])

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
                for i in range(int(n.group(1))):
                    expre+="(\w+),"
                for i in range(int(n.group(2))-int(n.group(1))):
                    expre+="(\w*),"
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
                    dict[cabeçalho[i]]=[new_dict[grupo+"0"]]
                    j=i
                    key = grupo+str(j)
                    while key in new_dict.keys():
                        dict[cabeçalho[i]].append(new_dict[key])
                        j+=1
                        key = grupo+str(j)
        
            lista.append(dict)

    return lista
    

def main():
    path="myheart.csv"
    set = parse(path)
    json(set)
                


if __name__ == '__main__':
    main()
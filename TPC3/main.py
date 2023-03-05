import re
from aux1 import*

def parse(path):
    file = open(path,"r")
    lines = file.read().split('\n')

    #onde vai ser armazenado o dataset
    #e uma lista de pessoas, cada pessoa vai ser uma lista em que -> [int Processo | int [Ano | mes | dia ] | str Nome | str Pai | str Mãe | str Observações]
    pessoas = []
    #vai servir para eliminar linhas repetidas
    pessoas_rep={}
    #vai servir para eliminar linhas invalidas(tou a considerar que todos os campos tem de tar prenchidos execpto o ultimo)
    reg_exp = r"^(\d+)::(\d{4}-\d{2}-\d{2})::((\w+ )*(\w+))::((\w+ )*(\w+))::((\w+ )*(\w+))::(.*)::$"

    for line in lines:
        if re.match(reg_exp,line):
            coluna = re.split(r"::",line)
            coluna.pop()
            data = re.split(r"-",coluna[1])
            coluna[1]=list(map(int,data))
            coluna[0]=int(coluna[0])
  
            if coluna[2] in pessoas_rep:#existe pelo menos uma pessoa com esse nome, podendo ser a mesma pessoa(repetida)
                igual = False
                for pessoa in pessoas_rep[coluna[2]]:
                    if coluna == pessoa:
                        igual = True
                        break
                if not igual:#se entrar aqui significa que existe outra pessoa com o mesmo nome(nao repetida)
                    pessoas_rep[coluna[2]].append(coluna)
                    pessoas.append(coluna)
            else:
                pessoas_rep[coluna[2]]=[coluna]
                pessoas.append(coluna)

    return pessoas

def main():
    path="processos.txt"
    pessoas = parse(path)

    option =0
    while option != -1:
        option=int(input("""
0 - frequência de processos por ano
1 - TOP 5 nomes próprios
2 - TOP 5 apelidos
3 - frequência dos tipos de relação ( irmão, sobrinho...)
4 - Converta os 20 primeiros registos num novo ficheiro de output em formato Json
else - exit
        """))
        if option == 0:
            print_tabelas(frequencia(pessoas,"Processo",1),1)
        elif option == 1:
            print_tabelas(TOP(frequencia(pessoas,"nome propio",100),5),2)
        elif option == 2:
            print_tabelas(TOP(frequencia(pessoas,"apelido",100),5),2)
        elif option == 3:
            None
        elif option == 4:
            None
        else:
            option = -1
                


if __name__ == '__main__':
    main()
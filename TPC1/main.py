from cache import Cache

def main():
    tabela = Cache()
    path="myheart.csv"
    file = open(path,"r")
    lines = file.read().split('\n')
    for line in lines:
        tabela.add(line)
    tabela.print()
    tabela.exc1()
    tabela.exc2()
    tabela.exc3()


if __name__ == '__main__':
    main()
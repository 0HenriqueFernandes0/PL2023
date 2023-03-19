import re
from aux1 import*
def main():
    #0-LEVANTAR -> 1,3
    #1-MOEDA -> 2,3
    #2-T= -> 2,3,4
    #3-ABORTAR -> 0
    #4-PAUSAR -> 0
    #5- fechar pograma(nao é um estado como os outros)
    Estado = 4
    saldo = 0
    while Estado < 5 :
        text = input()
        if Estado == 0:
            m = re.match("MOEDA( \d+,)*( \d)",text)
            if m:
                saldo = inserir(m)
                Estado = 1
            elif re.match("ABORTAR",text):
                Estado = 3
            else:
                print("Só pode inserir moedas ou entao abortar.")
        elif Estado == 1:
            m = re.match("T=(\d+)",text)
            if m:
                saldo-= ligar(m.group(1))
                Estado = 2
            elif re.match("ABORTAR",text):
                Estado = 3
            else:
                print("Só pode ligar ou entao abortar.")
        elif Estado == 2:
            m = re.match("T=(\d+)",text)
            if m:
                saldo-= ligar(m.group(1))
            elif re.match("ABORTAR",text):
                Estado = 3
            elif re.match("PAUSAR",text):
                Estado = 4
            else:
                print("Só pode ligar ou entao pousar/abortar.")
        elif Estado == 3 or Estado == 4:
            if re.match("LEVANTAR",text):
                Estado = 0
            else:
                print("Telefone ainda nao foi levantado.")



if __name__ == '__main__':
    main()
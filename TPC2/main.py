
def main():
    ON = True
    contador = 0
    while(1):
        text = input("Escreva o seu texto\n")

        start_ON_OFF= False
        of_signal=0

        for charecter in text:

            if charecter == "O" or charecter == "o":
                start_ON_OFF = True
            elif start_ON_OFF == True:
                if charecter == "N" or charecter == "n" and of_signal==0:
                    ON = True
                    start_ON_OFF = False
                elif charecter == "F" or charecter == "f":
                    if of_signal == 0:
                        of_signal +=1
                    elif of_signal == 1:
                        ON = False
                        start_ON_OFF = False
                        of_signal = 0
                else:
                    start_ON_OFF = False
                    of_signal = 0

            if charecter == "=":
                print(f"Soma: {contador}")
            if ON == True and charecter.isdigit():
                contador += int(charecter)


if __name__ == '__main__':
    main()
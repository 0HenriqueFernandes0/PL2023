class Cache:
    tabela = []

    def add(self, str):
        lines = str.split(",")
        if len(lines) > 5:
            if lines[0].isdigit():
                if lines[1] == "F" or lines[1] == "M":
                    if lines[2].isdigit() and int(lines[2]) > 0:
                        if lines[3].isdigit() and int(lines[3]) > 0:
                            if lines[4].isdigit() and int(lines[4]) > 0:
                                if lines[5].isdigit() and (int(lines[5]) == 0 or int(lines[5]) == 1):
                                    self.tabela.append(lines)

    def print(self):
        for line in self.tabela:
            print(";".join(line))

    def exc1(self):
        homens = 0
        muheres = 0
        for pessoa in self.tabela:
            if pessoa[1] == "M" and pessoa[5] == "1":
                homens += 1
            elif pessoa[1] == "F" and pessoa[5] == "1":
                muheres += 1
        print("Distribuição da doença por sexo: \nHomens: " + str(
            (homens / (homens + muheres)) * 100) + "% " + "\nMulheres: " + str(
            (muheres / (homens + muheres)) * 100) + "%")

    def exc2(self):
        escaloes = []
        total = 0
        for pessoa in self.tabela:
            if pessoa[5] == "1":
                for i in range(int(pessoa[0]) // 5 - len(escaloes)-5):
                    escaloes.append(0)
                total+=1
                escaloes[int(pessoa[0]) // 5 -6] += 1
        print("Distribuição da doença por escalões etários:")
        i=0
        for escalao in escaloes:
            print(f"[{i*5+30}-{i*5+34}]:{escalao/total*100}%")
            i+=1

    def exc3(self):
        escaloes = []
        total = 0
        for pessoa in self.tabela:
            if pessoa[5] == "1":
                for i in range(int(pessoa[3]) // 10 - len(escaloes)+1):
                    escaloes.append(0)
                total+=1
                escaloes[int(pessoa[3]) // 10 ] += 1
        print("Distribuição da doença por escalões etários:")
        i=0
        for escalao in escaloes:
            print(f"[{i*10}-{i*10+9}]:{escalao/total*100}%")
            i+=1



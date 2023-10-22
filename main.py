# # # # class cachorro:
# # # #     def __init__(self, nome, raca, peso):
# # # #         self.nome = nome
# # # #         self.peso = peso
# # # #         self.raca = raca
    
# # # #     def comer(self):
# # # #         return "croc croc croc"

# # # # cachoro1 = cachorro(nome= "Dogão", raca= "Caramelho", peso= "34")
# # # # cachoro2 = cachorro(nome= "Gãodo", raca= "Srd", peso= "35")

# # # # print(f"O cachorro chamado {cachoro1.nome} é da raça {cachoro1.raca} e pesa {cachoro1.peso}: {cachoro1.comer()}")
# # # # print(f"O cachorro chamado {cachoro2.nome} é da raça {cachoro2.raca} e pesa {cachoro2.peso}: {cachoro2.comer()}")

# # # # class Gato:
# # # #     def __init__(self, nome, raca, peso):
# # # #         self.nome = nome
# # # #         self.raca = raca
# # # #         self.peso = peso


# # # #     def derrubar(self):
# # # #         return "Derrubou"
    
# # # # gato1 = Gato(nome= "Rato", raca= "srd", peso= "100")

# # # # print(f" O gato chamado {gato1.nome} é da raça {gato1.raca} e pesa {gato1.peso}: 0 {gato1.nome} {gato1.derrubar()} o objeto")

# # # class Tamagochi:
# # #     def __init__(self, nome, saude, energia):
# # #         self.nome = nome
# # #         self.saude = saude
# # #         self.energia = energia
# # #     def lutar(self, energia):
# # #         self.energia = self.energia - 10
# # #         return self.energia
        
# # #     def brincar(self, energia):
# # #        self.energia = self.energia - 10
# # #        return self.energia
    
# # #     def comer(self):
# # #         self.energia = self.energia + 10
# # #         return self.energia
    
# # #     def descansar(self):
# # #        self.energia = self.energia + 10
# # #        return self.energia
    
# # # tama1 = Tamagochi(nome= "tamazão", saude="100", energia="100")



# # # nome = str(input("Digite o nome de seu Tamagoshi:"))
# # # energia = int(input("Digite a energia inicial de seu tamagochi: "))
# # # saude = int(input("Digite a saúde inicial de seu tamagochi: "))

# # # tamagotchi = Tamagochi(nome=nome, saude=saude, energia=energia)


# # # while True:
# # #     menu = int(input(f"""
# # #             Bem vindo {tamagotchi1.nome}
# # #             Saúde atual: {tamagotchi1.saude}
# # #             Energia atual: {tamagotchi1.energia}

# # #             1 - Brincar
# # #             2 - Lutar
# # #             3 - Comer
# # #             4 - Descansar
# # #             0 - Sair
# # #     """))

# # #     match menu:
# # #         case 1:
# # #             tamagotchi1.brincar()
# # #         case 2:
# # #             tamagotchi1.lutar()
# # #         case 3:
# # #             tamagotchi1.comer()
# # #         case 4:
# # #             tamagotchi1.descansar()
# # #         case 0:
# # #             break
# # #         case _:
# # #             print("Opção inválida")


# # class Tamagotchi:
# #     def __init__(self, nome:str, saude:int, energia:int):
# #         self.nome = nome
# #         self.saude = saude
# #         self.energia = energia
    
# #     def brincar(self):
# #         self.energia = self.energia - 10
# #         return self.energia

# #     def lutar(self):
# #         self.energia = self.energia - 20
# #         return self.energia
    
# #     def comer(self):
# #         self.energia = self.energia + 10
# #         return self.energia
    
# #     def descansar(self):
# #         self.energia = self.energia + 20
# #         return self.energia
        
# # nome = str(input("Digite o nome: "))
# # saude = int(input("Digite a saúde inicial: "))
# # energia = int(input("Digite a energia inicial: "))

# # tamagotchi1 = Tamagotchi(nome=nome, saude=saude, energia=energia)

# # while True:
# #     menu = int(input(f"""
# #             Bem vindo {tamagotchi1.nome}
# #             Saúde atual: {tamagotchi1.saude}
# #             Energia atual: {tamagotchi1.energia}

# #             1 - Brincar
# #             2 - Lutar
# #             3 - Comer
# #             4 - Descansar
# #             0 - Sair
# #     """))

# #     match menu:
# #         case 1:
# #             tamagotchi1.brincar()
# #         case 2:
# #             tamagotchi1.lutar()
# #         case 3:
# #             tamagotchi1.comer()
# #         case 4:
# #             tamagotchi1.descansar()
# #         case 0:
# #             break
# #         case _:
# #             print("Opção inválida")


# # class Animal_domestico():
# #     def __init__(self, nome, raca, peso):
# #         self.nome = nome
# #         self.raca = raca
# #         self.peso = peso 


# # class Cachorro(Animal_domestico):
# #     def __init__(self, nome, raca, peso):
# #         super().__init__(nome, raca, peso)

# class Animal_domestico:
#     def __init__(self, nome, raca, peso):
#         self.nome = nome
#         self.raca = raca
#         self.peso = peso

# class Cachorro(Animal_domestico):
#     def __init__(self, nome, raca, peso, coisa_nova):
#         super().__init__(nome, raca, peso)
#         self.coisa_nova = coisa_nova

#     def comer(self):
#         return "croc croc croc"

# class Gato(Animal_domestico):
#     def __init__(self, nome, raca, peso, instinto):
#         super().__init__(nome, raca, peso)
#         self.instinto = instinto

#     def derrubar(self):
#         return f"O {self.nome} derrubou algo"

# gato1 = Gato(nome="Alfredo", raca="Persa", peso=2, instinto=8001)
# cachorro1 = Cachorro(nome="Seila", raca="Vira lata", peso=3, coisa_nova="Alguma coisa")
    

class Conta:
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

def verificar(self):
    return f"""

    Nome = {nome}
    Número = {numero}
    Saldo = {saldo}

    """










numero = int(input("Digite um número: "))
nome = str(input("Digite seu nome: "))
saldo = float(input("Digite seu saldo: "))
        
        class Conta:
    def __init__(self, id:int, nome:str, saldo:float):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def visualizar_infos(self):
        return f"""
            Identificador: {self.id}
            Nome do Títular: {self.nome}
            Saldo da conta: {self.saldo}
        """
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
class Corrente(Conta):
    def __init__(self, id: int, nome: str, saldo: float):
        super().__init__(id, nome, saldo)

        def sacar(self, valor):
            self.saldo = self.saldo - valor
            return self.saldo
        
class Poupanca(Conta):
    def __init__(self, id: int, nome: str, saldo: float, juros:float):
        super().__init__(id, nome, saldo)
        self.juros = juros



while True:
    menu = int(input("""
            Bem vindo
            1 - Criar conta Corrente
            2 - Criar conta Poupança
            0 - Sair
    """))

    match menu:
        case 1:
            identificador = int(input("Digite o id: "))
            nome = str(input("Digite o nome do títular: "))
            saldo = float(input("Digite o saldo inicial: "))

            conta1 = Corrente(id=identificador, nome=nome, saldo=saldo)

        case 2:

            identificador = int(input("Digite o id: "))
            nome = str(input("Digite o nome do títular: "))
            saldo = float(input("Digite o saldo inicial: "))
            juros = float(input("Digite o juros: "))

            conta2 = Poupanca(id=identificador, nome=nome, saldo=saldo, juros=juros)
        case 0:
            break

        case _:
            print("Opção Inválida")
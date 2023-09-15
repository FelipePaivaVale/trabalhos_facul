import math

#Anthony Anderson Freitas da Silva
#Samuel Lima Souza
#Felipe de Paiva Vale
#Gustavo Henrique Bezerra de Medeiros

tamanho_disco = 2048
tamanho_bloco = 8

class Arquivo:
    def __init__(self, nome, tam, primeiro_bloco, blocos_ocupados):
        self.nome = nome
        self.tam = tam
        self.primeiro_bloco = primeiro_bloco
        self.ultimo_bloco = primeiro_bloco + blocos_ocupados - 1

    def __str__(self):
        return f"Nome: {self.nome}\nTamanho: {self.tam} bytes\nBlocos: {self.primeiro_bloco}-{self.ultimo_bloco}"

class Simulador:
    def __init__(self):
        self.disco = [0] * tamanho_disco
        self.arquivos = []

    def criar_arquivo(self):
        nome = input("Digite o nome do arquivo: ")

        if self.buscador(nome):
            print("Já existe um arquivo com esse nome.")
            return

        tam = int(input("Digite quantos bytes tem o arquivo: "))

        total_de_blocos = math.ceil(tam / tamanho_bloco)

        primeiro_bloco = self.espaço_livre(total_de_blocos)

        if primeiro_bloco == -1:
            print("Não há espaço suficiente para armazenar.")
            return

        for bloco in range(primeiro_bloco, primeiro_bloco + total_de_blocos):
            self.disco[bloco] = 1

        arquivo = Arquivo(nome, tam, primeiro_bloco, total_de_blocos)
        self.arquivos.append(arquivo)

        print("Arquivo criado com sucesso.")

    def remover(self):
        nome = input("Digite o nome do arquivo a ser removido: ")

        arquivo = self.buscador(nome)

        if arquivo:

            for bloco in range(arquivo.primeiro_bloco, arquivo.ultimo_bloco + 1):
                self.disco[bloco] = 0

            self.arquivos.remove(arquivo)

            print("Arquivo removido com sucesso.")
        else:
            print("Arquivo não encontrado.")

    def mostrar_arquivo(self):
        nome = input("Digite o nome do arquivo: ")

        arquivo = self.buscador(nome)

        if arquivo:
            print(arquivo)
        else:
            print("Arquivo não encontrado.")

    def desfragmentar(self):
        arquivos = []
        bloco_i = 0

        for arquivo in self.arquivos:

            for bloco in range(arquivo.primeiro_bloco, arquivo.ultimo_bloco + 1):
                self.disco[bloco] = 0

            arquivo.primeiro_bloco = bloco_i
            arquivo.ultimo_bloco = bloco_i + math.ceil(arquivo.tam / tamanho_bloco) - 1

            for bloco in range(arquivo.primeiro_bloco, arquivo.ultimo_bloco + 1):
                self.disco[bloco] = 1
        
            bloco_i = arquivo.ultimo_bloco + 1
            arquivos.append(arquivo)

        self.arquivos = arquivos

        print("Desfragmentação completa.")

    def espaço_livre(self, blocos_do_arquivo):
        inicio = -1
        livres = 0

        for i in range(tamanho_disco//tamanho_bloco):
            if self.disco[i] == 0:
                if livres == 0:
                    inicio = i

                livres +=1

                if livres == blocos_do_arquivo:
                    return inicio
            else:
                livres = 0
                inicio = -1

            if(tamanho_disco // tamanho_bloco - i) < blocos_do_arquivo - livres:
                return -1

        return -1

    def buscador(self, nome):
        for arquivo in self.arquivos:
            if arquivo.nome == nome:
                return arquivo
        return None
    
    def verificar_blocos(self):
        print("Estado atual dos blocos:")

        for i in range(0, math.ceil(tamanho_disco/tamanho_bloco)):
            bloco = self.disco[i]
            estado = " ".join(str(bloco))
            print(f"Bloco {i}: {estado}")

def main():
    simu = Simulador()

    while True:
        print("\n- Simulador de Gerência de Sistemas de Arquivos -")
        print("1-Criar arquivo")
        print("2-Remover arquivo")
        print("3-Exibir informações de arquivo")
        print("4-Desfragmentar")
        print("5-Exibir estado dos blocos")
        print("0-Sair")

        opc = input("Digite o número da opção desejada: ")

        if opc == "1":
            simu.criar_arquivo()
        elif opc == "2":
            simu.remover()
        elif opc == "3":
            simu.mostrar_arquivo()
        elif opc == "4":
            simu.desfragmentar()
        elif opc == "5":
            simu.verificar_blocos()    
        elif opc == "0":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
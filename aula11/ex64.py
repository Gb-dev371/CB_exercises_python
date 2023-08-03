# 64 - Crie uma função chamada "read_file" que recebe o nome de um arquivo e
# tenta abri-lo para leitura. Se o arquivo não existir, capture a exceção
# FileNotFoundError e imprima uma mensagem amigável para o usuário.

def read_file():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")
        return None


read_file()

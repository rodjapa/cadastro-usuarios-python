# 📌 Sistema de Cadastro de Usuários
# 🔹 Armazena nome, idade e profissão
# 🔹 Salva os dados em um arquivo
# 🔹 Permite consulta dos usuários cadastrados

# Criando uma lista para armazenar os usuários
usuarios = []

# 🔹 Função para cadastrar um novo usuário
def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    profissao = input("Digite a profissão: ")

    # Criando um dicionário para armazenar os dados
    usuario = {"Nome": nome, "Idade": idade, "Profissão": profissao}
    usuarios.append(usuario)

    print(f"\n✅ Usuário {nome} cadastrado com sucesso!\n")
    salvar_dados()  # Salvando no arquivo

# 🔹 Função para listar todos os usuários cadastrados
def listar_usuarios():
    if not usuarios:
        print("\n⚠️ Nenhum usuário cadastrado.\n")
        return
    
    print("\n📋 Lista de Usuários Cadastrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['Nome']}, Idade: {usuario['Idade']}, Profissão: {usuario['Profissão']}")
    print()

# 🔹 Função para salvar os dados em um arquivo
def salvar_dados():
    with open("usuarios.txt", "w") as arquivo:
        for usuario in usuarios:
            arquivo.write(f"{usuario['Nome']},{usuario['Idade']},{usuario['Profissão']}\n")

# 🔹 Função para carregar os dados do arquivo ao iniciar o sistema
def carregar_dados():
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                nome, idade, profissao = linha.strip().split(",")
                usuarios.append({"Nome": nome, "Idade": int(idade), "Profissão": profissao})
    except FileNotFoundError:
        pass  # Se o arquivo não existir, inicia com lista vazia

# 🔹 Função principal do sistema
def menu():
    carregar_dados()
    
    while True:
        print("\n📌 MENU DO SISTEMA")
        print("1️⃣ Cadastrar usuário")
        print("2️⃣ Listar usuários")
        print("3️⃣ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print("\n✅ Saindo do sistema...\n")
            break
        else:
            print("\n⚠️ Opção inválida! Tente novamente.\n")

# 🔹 Executando o sistema
menu()

continuar = True

while continuar:
    print("--- Gerenciador de Alunos ---")
    print("Digite 1 para Cadastrar novo aluno")
    print("Digite 2 para Listar alunos cadastrados")
    print("Digite 3 para Buscar aluno")
    print("Digite 4 Remover aluno")
    print("Digite 0 para Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = str(input("Digite o nome do Aluno: "))
        email = str(input("Digite o email do Aluno: "))
        curso = str(input("Digite o curso do Aluno: "))

        arquivo = open("alunos.txt", "a")
        arquivo.write(nome + ";" + email + ";" + curso + "\n")
        arquivo.close()

        print ("Aluno cadastrado com sucesso")

    elif opcao == 2:
        arquivo = open("alunos.txt", "r")
        alunos = arquivo.readlines()
        arquivo.close()

        if not alunos:
            print("Nenhum Aluno cadastrado")
        else:
            for aluno in alunos:
                dados = aluno.strip().split(";")
                print(f"Nome: {dados[0]} | Email: {dados[1]} | Curso: {dados[2]}")

    elif opcao == 3:
        nome_busca = input("Digite o nome do aluno para buscar: ")
        encontrado = False

        arquivo = open("alunos.txt", "r")
        for aluno in arquivo:
            dados = aluno.strip().split(";")
            if nome_busca.lower() in dados[0].lower():
                print(f"Encontrado: Nome: {dados[0]} | Email: {dados[1]} | Curso: {dados[2]}")
                encontrado = True
        arquivo.close()

        if not encontrado:
            print("Aluno não encontrado.\n")

    elif opcao == 4:
        nome_remover = input("Digite o nome do aluno para remover: ")
        novos_dados = []
        removido = False

        arquivo = open("alunos.txt", "r")
        for aluno in arquivo:
            dados = aluno.strip().split(";")
            if nome_remover.lower() not in dados[0].lower():
                novos_dados.append(aluno)
            else:
                removido = True
        arquivo.close()

        arquivo = open("alunos.txt", "w")
        arquivo.writelines(novos_dados)
        arquivo.close()

        if removido:
            print("Aluno removido com sucesso!\n")
        else:
            print("Aluno não encontrado.\n")

    elif opcao == 0:
        continuar = False
        print ("Encerrando Programa")

    else:
        print("Opção invalida")

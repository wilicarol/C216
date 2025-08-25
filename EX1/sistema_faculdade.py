alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")
    matricula = f"{curso}{len([a for a in alunos if a['curso'] == curso]) + 1}"
    alunos.append({"nome": nome, "email": email, "curso": curso, "matricula": matricula})
    print(f"Aluno {nome} cadastrado com matrícula {matricula}.")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Matrícula: {aluno['matricula']}, Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}")
    
def atualizar_aluno():
    print("CASO NÃO QUEIRA ALTERAR ALGUM CAMPO, DEIXE EM BRANCO!")
    matricula = input("Digite a matrícula do aluno que deseja atualizar: ")
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            nome = input("Digite o novo nome do aluno: ")
            email = input("Digite o novo e-mail do aluno: ")
            if nome:
                aluno["nome"] = nome
            if email:
                aluno["email"] = email
            print(f"Aluno com matrícula {matricula} atualizado.")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno que deseja remover: ")
    for i, aluno in enumerate(alunos):
        if aluno["matricula"] == matricula:
            del alunos[i]
            print(f"Aluno com matrícula {matricula} removido.")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\n Menu de Opções:"
              "\n 1. Cadastrar aluno"
              "\n 2. Listar alunos"
              "\n 3. Atualizar aluno"
              "\n 4. Remover aluno"
              "\n 5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno() 
        elif opcao == '5':
            print("Saindo do Sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__": 
    main()
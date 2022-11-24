# Nesse Exemplo as credenciais de login estão pre-definidas com as variáveis (login_s e senha_s)

while True:
    login = input("Digite o seu nome: ")
    senha = input("Digite a senha: ")

    login_s = "Usuario"  # Login Pré-definido
    senha_s = "123"  # Senha Pré-definida

    if login == login_s and senha == senha_s:
        print("Acesso Permitido")
        break

    elif login != login_s or senha != senha_s:
        print("Uma ou ambas credenciais são inválidas!")
        continue

    else:
        print("Erro")
        continue

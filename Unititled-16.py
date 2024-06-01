# Definindo a senha
senha_correta = "1234"

# Inicializando o número máximo de tentativas
tentativas_maximas = 3

# Loop para solicitar a senha
for tentativa in range(tentativas_maximas):
    senha_digitada = input("Digite sua senha: ")
    
    # Verificando se a senha está correta
    if senha_digitada == senha_correta:
        print("Bem-vindo.")
        break  # Encerra o loop se a senha estiver correta
    else:
        tentativas_restantes = tentativas_maximas - (tentativa + 1)
        if tentativas_restantes == 0:
            print("Senha incorreta. Seu telefone foi bloqueado.")
        else:
            print("Senha incorreta. Tentativas restantes:", tentativas_restantes)
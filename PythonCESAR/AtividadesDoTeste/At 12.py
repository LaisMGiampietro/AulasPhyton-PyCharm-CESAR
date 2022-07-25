nome = input('Digite seu nome de usuario:')
senha = input('Digite sua nova senha:')

while nome == senha:
    print('Senha inválida!')
    senha = input('Digite novamente uma senha:')
print("Usuario criado com sucesso!!")

login = input("Faça login com seu usuario:")
senha2 = input("Digite sua senha")

while login != nome or senha2 != senha:
    print('Senha inválida!')
    login = input("repita os dados:")
    senha2 = input("Digite sua senha")
print (f"Seja bem-vindo {login}!")
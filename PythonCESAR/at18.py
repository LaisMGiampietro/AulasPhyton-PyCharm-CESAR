"""Atividade 18
Façam um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações"""

nome = input('Digite seu nome de usuario:')
senha = input('Digite sua nova senha:')

while nome == senha:
    print('Senha inválida!')
    senha = input('Digite novamente uma senha:')

print('Login criado com sucesso!!')

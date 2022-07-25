"""Atividade 55
- Façam uma classe pessoa com:
- Atributos:nome, idade e telefone
- Métodos: mudar_numero (muda o número de telefone) e envelhecer(aumenta a idade)"""


class Pessoa:
    def __init__(self, nome, idade, tel):
        self.nome = nome
        self.idade = idade
        self.tel = tel

    def tel_mudar(self, tel):
        self.tel = tel

    def idade_mudar(self, idade):
        if idade > self.idade:
            self.idade = idade
            return
        print("A idade de entrada deve ser maio que a idade atual.")


pess = Pessoa("Lais", 24, 88118671)
pess.tel_mudar(88168171)
pess.idade_mudar(25)

"""Atividade 39
- Façam um programa que imprima o valor de “notas” dos dicionários abaixo.

dicionario = {
"turma": {
"estudante": {
"nome": "Marcos",
"notas": {
"matemática": 70,
"geografia": 80
}
}
}
}
}"""

dicionario = {
  "turma": {
      "estudante": {
          "nome": "Marcos",
          "notas": {
              "matemática": 70,
              "geografia": 80
          }
      }
  }
}
print(dicionario["turma"]["estudante"]["notas"])

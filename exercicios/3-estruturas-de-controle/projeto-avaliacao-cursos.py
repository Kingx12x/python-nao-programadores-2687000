competências = ['Python', 'PowerBI', 'SQL', 'R', 'Scrum' ]

print('----------------------------------')
linguagens_de_programacao = 'Python'
data = 'SQL'
tool = 'PowerBi'


Habilidades = {}

if data in competências:
  print(f"A competência {data}, está disponível. Avalie o curso")
  Habilidades[data] = int(input(f'Qual seria a nota para esse curso?(0 a 5) '))

if tool in competências:
  print(f"A competência {tool}, está disponível. Avalie o curso")
  Habilidades[tool] = int(input(f'Qual seria a nota para esse curso?(0 a 5) '))

if linguagens_de_programacao in competências:
  print(f"A competência {linguagens_de_programacao}, está disponível. Avalie o curso")
  Habilidades[linguagens_de_programacao] = int(input(f'Qual seria a nota para esse curso?(0 a 5) '))
else:
  print("Você ainda não aprendeu essa habilidade")  

print(Habilidades)






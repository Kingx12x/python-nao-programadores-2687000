A= 33
B= 40
C= 66
D= 330

if A < B:
  print(f'A condição foi atingida, pois {A}, é menor que {B}')

else:
  print(False)

if A == D:
  print(f'A condição foi cumprida. {A} é igual a {D}')
elif A > D:
 print(f'Nesse caso verifcamos que {A}, é maior que {D}')



if (C > D) or (D == A):
  print(f'A condição foi concluida pois {C}. é maior que {D}')
elif(B > C) and (D < A):
  print(f'A condição não foi concluida pois {B}, é menor que {C}')
else:
  print(f'Nenhuma das condições foram concluidas')


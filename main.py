a = int(input('A háromszög a oldalának hossza? '))
b = int(input('A háromszög b oldalának hossza? '))
c = int(input('A háromszög c oldalának hossza? '))
if a+b>c and a+c>b and b+c>a:
  kiírandó = 'A háromszög megszerkeszthető. '
else:
  kiírandó = 'A háromszög nem szerkeszthető meg. '
print(kiírandó)
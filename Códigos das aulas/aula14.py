a = 'A'
b = 'B'
c = 1.1
string =' a={0} b={1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
    )
# Tudo que vier dps de um parametro nomeado precisa ser nomeado.
print(formato)

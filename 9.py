n = int(input('Входные данные (кол-во школьников): '))
k = int(input('Входные данные (кол-во мандаринов): '))
c = k // n
v = k % n
print('мандарины у школьников:', c)
print('мандарины в корзине:', v)
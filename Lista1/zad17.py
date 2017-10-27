lista = [x**2 for x in range(100)]

print('\n'.join('{} -> {}'.format(*k) for k in enumerate(lista)))
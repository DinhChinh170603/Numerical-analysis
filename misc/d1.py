a = 3.7495
b = 2.547
delta_a = float( 5 * 10 ** - 4)
delta_b = float(10 ** - 3)

u = a * b

print(f'sai so tuong doi a: {delta_a / a}')
print(f'sai so tuong doi b: {delta_b / b}')

delta_u = ( (a + delta_a)  * (b + delta_b) - (a - delta_a) * (b - delta_b) ) / 2
print(f'u: {u}')
print(f'delta_u: {delta_u}')
print(f'sai so tuong doi cua u: {delta_u / u}')
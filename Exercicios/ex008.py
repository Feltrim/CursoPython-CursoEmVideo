print('Conversor de Medidas\n')

m = float(input('Insira um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'{m}m é equivalente a {km}km')
print(f'{m}m é equivalente a {hm}hm')
print(f'{m}m é equivalente a {dam}dam')
print(f'{m}m é equivalente a {dm}dm')
print(f'{m}m é equivalente a {cm}cm')
print(f'{m}m é equivalente a {mm}mm')

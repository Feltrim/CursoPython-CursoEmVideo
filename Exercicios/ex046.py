from time import sleep


print('Contagem regressiva\n')

print('O show de fogos de de artifício começará em:\n')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('\nCOMEÇOU!!!')

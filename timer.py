from time import sleep


seconds = int(input('Type how many seconds it is to wait:'))
print("I'll start in")

sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('Waiting...')

for cont in range(seconds, -1, -1):
    print(cont)
    sleep(1)
print('Finish')

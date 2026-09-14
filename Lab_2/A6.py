N = int(input('Введите количество секунд: '))

hours = (N // 3600) % 24
minutes = (N % 3600) //  60
seconds = N % 60

print('{}:{:02}:{:02}'.format(hours, minutes, seconds))

import math
while True:
    i = input( 'Если хотите найти сторону треугольника, нажмите (1) \nЕсли хотите выйти, нажмите (2)')
    if i == "1":
        a = float( input( ' Введите сторону 1-ую известную сторону треугольника '))
        b = float( input( ' Введите 2-ую известную сторону треугольника '))
        c = float( input( ' Введите угол '))
        c = math.cos( c*math.pi/180)
        d = math.sqrt(a**2 + b**2 - 2*a*b*c)
        
        print( 'Результат: ' + str(d))           
    elif i == "2":
        break    
    else:
        print( 'Выбрана неверная операция')
     
                   
                   

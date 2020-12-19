a = float(input('Введите свой вес '))
b = float(input('Введите свой рост '))
result = int(a* 10000) / (b ** 2)

#if isinstance((a),int): 
   # print ("Ваш индекс массы тела : ",  round(float(result), 1))
#else:
    #print ('Введите данные в числовом формате') 
print ( "Ваш индекс массы тела : ",  round(float(result), 1))  
result = int(result)
first = int(result) - 16
scale = '16' + "=" * first + str(result) + "=" * (24 - first) + "40"


if result > 18.5 and result < 30: 
    print ('Нормальный индекс массы тела')
    print(scale)
elif result > 16 and result < 18.5:
    print ("Дефицит массы тела")
    print(scale)  
elif result > 30 and result < 40:
    print ("Ожирение")
    print(scale) 
elif result < 16 and result > 0:
    print ('Ярко выраженный дефицит массы тела')     
else :
    print ('Данные некорректны')    

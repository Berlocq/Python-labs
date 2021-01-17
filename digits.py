a = '\u2B1C'
b = '  '
ps = '\n'

zero = [(a*4), (a + b + b + a), (a + b + b + a), (a + b + b + a), (a*4)]
one = [(a*3 + b), (b + b + a + b), (b + b + a + b), (b + b + a + b), (a*4)]
two = [(a*4), (b + b + b + a), (a*4),(a + b + b + b), (a*4)]
three = [(a*4), (b + b + b + a), (a*4),(b + b + b + a), (a*4)]
four = [(a + b + b + a), (a + b + b + a), (a*4), (b + b + b + a), (b + b + b + a)]
five = [(a*4), (a + b + b + b), (a*4),(b + b + b + a), (a*4)]
six = [(a*4), (a + b + b + b), (a*4),(a + b + b + a), (a*4)]
seven = [(a*4), (b + b + b + a), (b + b + b + a), (b + b + b + a), (b + b + b + a)]
eight = [(a*4), (a + b + b + a), (a*4),(a + b + b + a), (a*4)]
nine = [(a*4), (a + b + b + a), (a*4),(b + b + b + a), (a*4)]
razdel = [(b*3), (b + a + b), (b*3), (b + a + b), (b*3)]

digit = {'0' : zero, '1' : one, '2' : two, '3' : three, '4' : four, '5' : five, '6' : six, '7' : seven, '8' : eight, '9' : nine, ':' : razdel}

for i in range (len(zero)):
    print(zero[i], one[i], razdel[i], two[i], three[i], razdel[i], four[i], five[i], six[i], seven[i], eight[i], nine[i], razdel[i])








#print('/n'.join(nine))
# print(zero[0] + ps + zero[1] + ps + zero[2] + ps + zero[3] + ps + zero[4])
# print(one[0] + ps + one[1] + ps + one[2] + ps + one[3] + ps + one[4])
# print(two[0] + ps + two[1] + ps + two[2] + ps + two[3] + ps + two[4])
# print(three[0] + ps + three[1] + ps + three[2] + ps + three[3] + ps + three[4])
# print(four[0] + ps + four[1] + ps + four[2] + ps + four[3] + ps + four[4])
# print(five[0] + ps + five[1] + ps + five[2] + ps + five[3] + ps + five[4])
# print(six[0] + ps + six[1] + ps + six[2] + ps + six[3] + ps + six[4])
# print(seven[0] + ps + seven[1] + ps + seven[2] + ps + seven[3] + ps + seven[4])
# print(eight[0] + ps + eight[1] + ps + eight[2] + ps + eight[3] + ps + eight[4])
# print(nine[0] + ps + nine[1] + ps + nine[2] + ps + nine[3] + ps + nine[4])
# print(razdel[0] + ps + razdel[1] + ps + razdel[2] + ps + razdel[3] + ps + razdel[4])
# range(10)
# (zero, one, two, three, four, five, six, seven, eight, nine) = range(10)
# print(razdel)



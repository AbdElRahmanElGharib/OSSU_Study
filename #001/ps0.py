
import numpy
import readchar


while True:

    try:
        n = float(input('Enter n:'))
        x = float(input('Enter the power:'))
        break
    except:
        print('---Enter a valid NUMBER---')


result_1 = n**x
result_2 = numpy.log2(n)

print('n**x =',result_1)
print('log2 of n =',result_2)

print('\n Press any key to exit')
readchar.readchar()

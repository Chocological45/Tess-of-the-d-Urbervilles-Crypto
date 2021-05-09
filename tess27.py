# Performs frequency analysis on the tess27.txt file in the case that the results differ from the general frequency analysis

import collections

with open('/Users/saptarshinath/Desktop/tess27.txt') as file:
    contents = file.read()

    frequency_analysis = collections.Counter(contents)

    sorted_x = sorted(frequency_analysis.items(), key=lambda kv: kv[1])
    #print(sorted_x)

    '''
    [('Z', 581), ('Q', 631), ('J', 657), ('X', 914), ('K', 5079), ('V', 6057), ('B', 9612), ('P', 9839), 
    ('Y', 12895), ('G', 13378), ('F', 14235), ('C', 15143), ('M', 15672), ('W', 15903), ('U', 18098), 
    ('L', 26461), ('D', 29708), ('R', 38489), ('S', 41869), ('I', 42774), ('N', 44210), ('H', 45380), 
    ('O', 48460), ('A', 50261), ('T', 58553), ('E', 84020), ('|', 151160)]

    '''
    contents = contents.replace('|', ' ')

    split = contents.split(' ')
    freq = collections.Counter(split).most_common()
    print(freq)








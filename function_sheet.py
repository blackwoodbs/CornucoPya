#CornucoPya

import catalog
import time

base = catalog.SuperBases
seq = ''

#FORMATTING INPUT SEQ
def format_seq():
    seq = input("enter your sequence: ")
    for x in base:
        for i in (base[x].get('common Names')):
            seq = seq.replace(i, base[x].get('inString')[0])

    print("Formatted Sequence = " + seq)
    return seq

#FUNCTION FOR RETRIVING DATA FROM DICTIONARY
def get_array(sequence, dictionary_key): #returns the transformed array

    destroy_seq = sequence
    desired_arr = []
    i = 0
    while i <= len(destroy_seq):
        for x in base:
            for j in (base[x].get('inString')):
                if destroy_seq[0:i] == j:
                    desired_arr.append(base[x].get(dictionary_key))
                    destroy_seq = destroy_seq.replace(j, '', 1)
                    i = 0
        i = i + 1

    # print('seq length = ' + str(len(destroy_seq)))
    # print('i = ' + str(i))
    print(destroy_seq)
    if len(destroy_seq) == 0:
        return (desired_arr)
    elif i == len(destroy_seq):
         return [61.97]
        #PLACEHOLDER FOR ERROR HANDLINGAT


formatted_sequence = format_seq()

mw = round(sum(get_array(formatted_sequence, 'incorporated MW')) - 61.97, 2) #61.97 = empirical correction
print('Molecular Weight = ' + str(mw))

test_arr = get_array(formatted_sequence, 'inString')
print(test_arr)

time.sleep(5)



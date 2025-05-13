#Average of floating values 
#e.g. X-DSPAM-Confidence:    0.8475
#file mbox-short.txt
fname = input('enter file name:')
file_acess = open(fname)
for line in file_acess:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        print('find' , line.find('0.'))
        

    print('line',line)
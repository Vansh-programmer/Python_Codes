#Average of floating values 
#e.g. X-DSPAM-Confidence:    0.8475
#file enter file name: C:\Users\vansh\OneDrive\Desktop\Python_Codes\Python Data Structures\mbox-short.txt

fname = input('enter file name:')
file_acess = open(fname)
total = 0
avg =0
value = 0
for line in file_acess:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        line.find('0.')
    value+=1
    data = float(line[20:])
    total +=data

avg = total/value
print(avg)
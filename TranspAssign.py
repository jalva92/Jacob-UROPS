seq = open('/Users/Jacob/sequences/chrI(1).fa','r').read()
transp = open('/Users/Jacob/sequences/ty5(1).fa','r').read()

import random
x = random.randint(0,len(seq))
p = random.randint(0,1)
o = random.randint(0,1)
#generates random position and random integral 0 or 1 in this case

if o == 1:
    transp = transp[::-1] + "0000000000"
#orientation based on 50% chance of reverse insertion
#row of 0's included to allow checking of direction of insertion, plus reverse compliment
    
#substitute 1 with desired probability
if p == 1:
    chrInew = seq[:x] + "----------" + transp + "----------" + seq[x:len(seq)]
    # "-------" included for ease of checking whether transp is inserted
else:
    chrInew = seq
    
test = open('/Users/Jacob/sequences/chrInew.fa','w')

for line in chrInew:
    str.strip("\n")
    test.write(line)

test = open('/Users/Jacob/sequences/chrInew.fa','r')
test.read()
#writes new chr into file
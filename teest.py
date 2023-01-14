key  = {'right':True,'up':False,'down':False,'left':False}

for dirc in key:
    if dirc =='right':
        key[dirc] = False
    else:
        key[dirc] = True
for ke in key:
    print(key.get(ke))
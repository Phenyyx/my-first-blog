import random

codes = []
unwanted = ['88', 'SS', 'NS', 'HH', 'HJ', 'AH', 'KZ']

i = 0
while i < 50000:
    x = random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')
    y = random.choice('1234567890')
    z = random.choice('1234567890')
    w = random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')
    v = random.choice('ABCDEFGHJKLMNPQRSTUVWXYZ')

    code = x + y + z + w + v
    
    if any(ele in code for ele in unwanted):
        pass
    else:
        if code in codes:
            pass
        else:
            codes.extend([code])
            i += 1

print(codes)
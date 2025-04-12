credito = {'123': 750, '789': 980}

score_123 = credito['123']
score_789 = credito['789']

print(score_123)
print(score_789)

credito['123'] = 435
print(credito)

credito['456'] = 1000
print(credito)
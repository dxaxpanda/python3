

d = {'test': 'Hello'}

try:
    print(d['tes']) # erreur typo
except Exception as e:
    print(d)
    raise e

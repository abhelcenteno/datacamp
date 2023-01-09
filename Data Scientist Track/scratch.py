z = {x:('good' if x==0 else (('worse' if x >= 5 else 'bad'))) for x in range(10)}

print(z)
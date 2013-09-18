import amazonapi
p = amazonapi.AMAZONAPI("9381626685") #10-digit ISBN code
if p.request() == True:
    print p.get_json()
else:
    print p.error


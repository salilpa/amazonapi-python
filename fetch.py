import amazonapi
p = amazonapi.AMAZONAPI("9382618341") #10-digit ISBN code
if p.request() == True:
    print p.get_json()
else:
    print p.error


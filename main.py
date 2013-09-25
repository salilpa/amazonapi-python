#!/usr/bin/env python
import sys
import amazonapi

def main(argv):
    for pnr in argv:
        p = amazonapi.AMAZONAPI(pnr) #10-digit ISBN code
        if p.request() == True:
            print p.get_json()
        else:
            print p.error

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'usage: main.py 9382618341 9381626685'
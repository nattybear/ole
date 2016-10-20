from header import bin2hex

fname = 'c:\\users\\user12\\ole\\FileHeader.dump'

fp = open(fname, 'rb')

signature = bin2hex(fp, 0, 32)

print 'signature : ', signature
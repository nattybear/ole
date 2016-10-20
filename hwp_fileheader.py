from struct import unpack
from StringIO import StringIO
from header import bin2hex
from property import property_list
from sbat import pnum2data, SBAT, fSDB

def get_bit(num, i):
    ret = (num & (1<<i)) != 0
    return ret

pdata = pnum2data(SBAT, property_list, 1, fSDB)
fpdata = StringIO(pdata)

fp = fpdata
    
signature = bin2hex(fp, 0, 32)

version = unpack('B'*4, bin2hex(fp, 32, 4))
version2 = list(version)
version2.reverse()
version3 = [str(x) for x in version2]

attrib = bin2hex(fp, 36, 4)
attrib2 = unpack('I', attrib)[0]

print 'signature : ', signature
print 'version : ', '.'.join(version3)
print 'compress : ', get_bit(attrib2, 0)
print 'password : ', get_bit(attrib2, 1)
print 'publish : ', get_bit(attrib2, 2)
print 'script : ', get_bit(attrib2, 3)
print 'DRM : ', get_bit(attrib2, 4)
print 'XML : ', get_bit(attrib2, 5)
print 'history : ', get_bit(attrib2, 6)
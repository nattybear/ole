from struct import unpack
from header import fp, bin2hex
from bbat import chain, read_block

def chain2storage(chain):
    storage = ''
    for i in chain:
        buf = read_block(fp, i, 0x200)
        storage += buf
    return storage
    
def single_property(fp, offset):
    i = offset + 0x40
    tmp = bin2hex(fp, i, 2)
    size_pname = hex2short(tmp)
    
    i = offset
    tmp = bin2hex(fp, i, size_pname)
    pname = tmp.replace(b'\x00', '')
    
    if size_pname == 0:
        return
    
    #print "Size of Property's name : ", size_pname
    print pname
    
    return
    
def hex2short(buf):
    return unpack('H', buf)[0]
    
def block2property(fp, block_num):
    i = block_num + 1
    i2 = i * 0x200
    for j in range(4):
        j2 = i2 + (j * 0x80)
        single_property(fp, j2)
    return
    
property_storage = chain2storage(chain)
property_list = []

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\property_storage.dump', 'wb')
    fp2.write(property_storage)
    fp2.close()
    
    print '[*] property_storage.dump saved'
    
    for i in chain:
        block2property(fp, i)
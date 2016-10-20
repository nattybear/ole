from struct import unpack
from StringIO import StringIO
from header import fp, bin2hex
from bbat import chain, read_block

class Property:
    def __init__(self, storage, num):
        i = num * 0x80
        
        size = bin2hex(storage, i+0x40, 2)
        self.size = unpack('H', size)[0]
        
        name = bin2hex(storage, i, self.size)
        self.name = name.replace(b'\x00', '')
        
        type = bin2hex(storage, i+0x42, 1)
        type = unpack('b', type)[0]
        if type == 1:
            self.type = 'storage'
        elif type == 2:
            self.type = 'stream'
        elif type == 5:
            self.type = 'root'
        else:
            self.type = None
            
        prev = bin2hex(storage, i+0x44, 4)
        self.prev = unpack('i', prev)[0]
        
        next = bin2hex(storage, i+0x48, 4)
        self.next = unpack('i', next)[0]
        
        dir = bin2hex(storage, i+0x4C, 4)
        self.dir = unpack('i', dir)[0]

def chain2storage(chain):
    storage = ''
    for i in chain:
        buf = read_block(fp, i, 0x200)
        storage += buf
    return storage
    
property_storage = chain2storage(chain)

fstorage = StringIO(property_storage)

test = Property(fstorage, 0)

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\property_storage.dump', 'wb')
    fp2.write(property_storage)
    fp2.close()
    
    print '[*] property_storage.dump saved'
    
    print 'Name : ', test.name
    print 'Type : ', test.type
    print 'Prev : ', test.prev
    print 'Next : ', test.next
    print 'Dir : ', test.dir
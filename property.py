from struct import unpack
from StringIO import StringIO
from header import fp, bin2hex
from bbat import chain, read_block

class Property:
    def __init__(self, storage, num):
        i = num * 0x80
        
        self.num = num
        
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
        
        start = bin2hex(storage, i+0x74, 4)
        self.start = unpack('i', start)[0]
        
        psize = bin2hex(storage, i+0x78, 4)
        self.psize = unpack('I', psize)[0]

def chain2storage(chain):
    storage = ''
    for i in chain:
        buf = read_block(fp, i, 0x200)
        storage += buf
    return storage
    
def size2count(size):
    count = size / (0x200 / 4)
    return count
    
property_storage = chain2storage(chain)
fstorage = StringIO(property_storage)

storage_size = len(property_storage)
count = size2count(storage_size)

property_list = []
for i in range(count):
    pro = Property(fstorage, i)
    t = {}
    t['name'] = pro.name
    t['type'] = pro.type
    t['prev'] = pro.prev
    t['next'] = pro.next
    t['dir'] = pro.dir
    t['start'] = pro.start
    t['psize'] = pro.psize
    property_list.append(t)

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\property_storage.dump', 'wb')
    fp2.write(property_storage)
    fp2.close()
    
    print '[*] property_storage.dump saved'
    print ''
    
    for i in range(count):
        test = Property(fstorage, i)
        if test.size == 0:
            break
        print '[' + str(i) + '] ', test.name
        print '  [-] Type : ', test.type
        print '  [-] Prev : ', test.prev
        print '  [-] Next : ', test.next
        print '  [-] Dir : ', test.dir
        print '  [-] Start : ', test.start
        print '  [-] Size : ', test.psize
    

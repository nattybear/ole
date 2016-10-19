from header import fp
from bbat import chain, read_block

def chain2storage(chain):
    storage = ''
    for i in chain:
        buf = read_block(fp, i, 0x200)
        storage += buf
    return storage
    
property_storage = chain2storage(chain)

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\property_storage.dump', 'wb')
    fp2.write(property_storage)
    fp2.close()
    
    print '[*] property_storage.dump saved'
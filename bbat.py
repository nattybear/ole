from struct import unpack
from header import fp, array_BBAT_depot_members, startblock_property


BBAT = '' # Big Block Allocation Table

def read_block(fp, num_block, size):
    num = num_block + 1
    offset = num * size
    fp.seek(offset)
    buf = fp.read(size)
    return buf
    
def array2table(fp, array, size):
    table = ''
    for i in array:
        buf = read_block(fp, i, size)
        table += buf
    return table
    
def read_entry(table, entry):
    i = entry * 4
    tmp = table[i:i+4]
    entry = unpack('i', tmp)[0]
    return entry
    
def table2chain(table, entry):
    chain = []
    while True:
        if entry == -3:
            print '[*] Special block'
            return chain
        elif entry == -2:
            #print '[*] End of chain'
            return chain
        elif entry == -1:
            print '[*] Useless block'
            return chain
        else:
            chain.append(entry)
            entry = read_entry(table, entry)
            
BBAT = array2table(fp, array_BBAT_depot_members, 0x200)
chain = table2chain(BBAT, startblock_property)

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\BBAT.dump', 'wb')
    fp2.write(BBAT)
    fp2.close()

    print '[*] BBAT.dump saved'
    
    chain2 = []
    for i in chain:
        chain2.append('Entry ' + str(i))
        
    print ' -> '.join(chain2)
from ole_headerblock_info import fp, array_BBAT_depot_members

BBAT = '' # Big Block Allocation Table

def read_block(fp, num_block, size):
    num = num_block + 1
    offset = num * 0x200
    fp.seek(offset)
    buf = fp.read(0x200)
    return buf
    
def array2table(fp, array, size):
    table = ''
    for i in array:
        buf = read_block(fp, i, 0x200)
        table += buf
    return table
    
BBAT = array2table(fp, array_BBAT_depot_members, 0x200)

fp2 = open('c:\\users\\user12\\ole\\BBAT.dump', 'wb')
fp2.write(BBAT)
fp2.close()

print '[*] BBAT.dump saved'
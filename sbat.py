from sys import argv
from header import startblock_SBAT, num_SBAT_depot, fp
from bbat import table2chain, BBAT, array2table
from property import property_list

print '[*] Start block of SBAT : ', startblock_SBAT
print '[*] Number of SBAT Depot : ', num_SBAT_depot

chain = table2chain(BBAT, startblock_SBAT)
SBAT = array2table(fp, chain, 0x200)

root_start = property_list[0]['start']
root_chain = table2chain(BBAT, root_start)

# Small Data Block
SDB = array2table(fp, root_chain, 0x200)

if __name__ == '__main__':
    fp2 = open('c:\\users\\user12\\ole\\SBAT.dump', 'wb')
    fp2.write(SBAT)
    fp2.close()
    
    print '[*] SBAT.dump saved'
    
    fp3 = open('c:\\users\\user12\\ole\\SBD.dump', 'wb')
    fp3.write(SDB)
    fp3.close()
    
    print '[*] SDB.dump saved'
    
    try:
        pnum = int(argv[1])
        pchain = table2chain(SBAT, property_list[pnum]['start'])
        print pchain
    except:
        pass
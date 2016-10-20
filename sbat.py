from sys import argv
from StringIO import StringIO
from header import startblock_SBAT, num_SBAT_depot, fp
from bbat import table2chain, BBAT, array2table
from property import property_list

#print '[*] Start block of SBAT : ', startblock_SBAT
#print '[*] Number of SBAT Depot : ', num_SBAT_depot

chain = table2chain(BBAT, startblock_SBAT)
SBAT = array2table(fp, chain, 0x200)

root_start = property_list[0]['start']
root_chain = table2chain(BBAT, root_start)

# Small Data Block
SDB = array2table(fp, root_chain, 0x200)
fSDB = StringIO(SDB)

def pnum2data(SBAT, list, pnum, fSDB):
    pnum2 = int(pnum)
    pchain = table2chain(SBAT, property_list[pnum2]['start'])
    pchain2 = [x - 1 for x in pchain]
    pdata = array2table(fSDB, pchain2, 0x40)
    return pdata

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
        pnum = argv[1]
        pdata = pnum2data(SBAT, property_list, argv[1], fSDB)
        
        fname = property_list[int(pnum)]['name'] + '.dump'
        fp4 = open(fname, 'wb')
        fp4.write(pdata)
        fp4.close()
        
        print '[*]', fname, 'saved'
    
    except:
        pass
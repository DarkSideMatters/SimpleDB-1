import sys

filename = 'database.txt'

dbdata = {1:'a', 2:'b', 3:'b'}
binarydb = bytearray(dbdata)

dbkey = sys.argv[1]
dbvalue = sys.argv[2]

## writing function - not working
#def set_db(key=dbkey,value=dbvalue):
#    filename.write("{} {}", format(key, value))
#   dbdata[dbkey] = dbvalue
#    binarydb = bytearray(dbdata)

def encwrite(key=dbkey, value=dbvalue):
    db = open(filename,'a')
    db.write(enc("{} {}",format(key,value)))
    #db.write(enc(dbvalue))
    db.close()

def enc(str):
	return ' '.join(format(ord(x), 'b') for x in str) + ' '

#with open(filename,'wb') as filedata:
#   filedata.write(enc(binarydb))

## reading function
def encread():
    r = open(filename, 'rb')
    content = r.read().decode('utf-8')
    content = ''.join(chr(int(content[i*8:i*8+8],2)) for i in range(len(content)//8))
    print(content)

if __name__ == "__main__":
    encwrite()
    encread()






    
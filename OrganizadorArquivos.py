url = 'C:/DESENVOLVIMENTO/OrganizadorArquivos/source_img'

from pathlib import Path
import datetime


directory = Path(url)
files = directory.glob('*.*')

#Obtem os anos dos arquivos
anos = [datetime.datetime.fromtimestamp(f.stat().st_mtime).year for f in files]

d = {x:anos.count(x) for x in anos}
print(d)


'''for ano in anos_a:
    print(ano)

for f in files:
    #print(f.stat().st_ctime)
    #print(datetime.datetime.fromtimestamp(f.stat().st_ctime))
    #print(datetime.datetime.fromtimestamp(f.stat().st_atime))
    print(datetime.datetime.fromtimestamp(f.stat().st_mtime))
'''


from datetime import datetime, timedelta
from multiprocessing import Pool
import multiprocessing as mp
import os

today = datetime.now() - timedelta(days=0)

server = 'https://s3-us-west-1.amazonaws.com//files.airnowtech.org/airnow/'

year = str(today.year)
m = str(today.month)

os.system('tar -xvzf {}.tgz'.format(m))
os.system('mkdir out')
os.chdir('out')

d = str(today.day)
hours = [str(i).zfill(2) for i in range(7, 23)]

def get(h):
    global year, server, m, d
    qstr = server + year + '/{}{}{}'.format(year, m.zfill(2), d.zfill(2)) + '/HourlyAQObs_{}{}{}{}.dat'.format(year, m.zfill(2), d.zfill(2), h)
    os.system('wget -N {}'.format(qstr))

p = Pool(mp.cpu_count())
p.map(get, hours)

os.chdir('..')
os.system('tar -I pigz -cf {}.tgz out'.format(m))
os.system('rm -rf out')


import os, shutil
import datetime
import pdb
name=raw_input("enter name")
date=raw_input("enter date")
time=int(raw_input("enter time"))
index="0000"
path=raw_input("enter the path")
if time =='':
   time = 0
try:
    cnt = 0
    t_cnt = 0
    for name in os.listdir(path):
        if (time == 0 or '0' in str(time)) and cnt <=9 :
           time = '0' + str(cnt)
        if cnt >=10:
            time = 10
            time = time + t_cnt 
            t_cnt += 1
        file_name=name+'_'+date+'_'+index+'.'+str(time)
        newfile = os.path.join(path, file_name)
        print time
        if time == 24:
            time =0
            tmp_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            tmp_date += datetime.timedelta(days=1)
            date=tmp_date.strftime('%Y-%m-%d')
            cnt  = 0
            t_cnt = 0
            continue
        cnt += 1
        print newfile
        
except:
    print "no files found"
    
    


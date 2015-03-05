import glob, sys

path_xgtf = sys.argv[1]
path_idx = sys.argv[2]
path_out = sys.argv[3]

def sync_idx(f_idx):
    dic_idx = {}
    for line in open(f_idx):
        frame, type, p, time = line.split()
        dic_idx[int(frame)] = float(time)
        max=int(frame)
        
    for i in range(max+10):
        time = i    
        if time not in dic_idx:
            while time not in dic_idx:
                time-=1     
                if time<1:
                    time = i
                    break
        if time not in dic_idx:                                    
            while time not in dic_idx:
                time+=1  
                
        
        if i not in dic_idx:
            dic_idx[i] = dic_idx[time]
    return dic_idx


for f_xgtf in glob.glob(path_xgtf+'/*.xgtf'):
    print f_xgtf

    video = f_xgtf.split('/')[-1].split('.')[0]

    dic_idx = sync_idx(path_idx+video+'.MPG.idx')
    fout = open(path_out+video+'.mdtm', 'w')

    data=False
    frame=0
    doc = []
    current_line=''
    for line in open(f_xgtf):
        if data:
            current_line+=line.replace('\n','')            
            if '</object>' in line or '</file>' in line:
                doc.append(current_line)
                current_line=''            
        if '<data>' in line:
            data=True      

    start_tete=False
    l_frame=[]
    for line in doc:
        line = line.replace('&lt;', '<')
        if 'name="PERSONNE"' in line:
            l = line.split('<attribute')  
            if 'framespan="' in l[0]:
                name=''
                startframe=''
                endframe='' 
                for a in l:
                    if 'name="NOM">' in a:
                        name= a.split('svalue value="')[1].split('"/>')[0]                    
                    if 'name="STARTFRAME">' in a:
                        startframe= a.split('dvalue value="')[1].split('"/>')[0]
                    if 'name="ENDFRAME">' in a:
                        endframe= a.split('dvalue value="')[1].split('"/>')[0]
                if name!='' and startframe!='' and endframe!='' : 
                    start = dic_idx[int(startframe)]
                    duration = dic_idx[int(endframe)] - start
                    fout.write(video+' 1 '+str(start)+' '+str(duration)+' head NA NA '+name+'\n')
    fout.close()



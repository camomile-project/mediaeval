import glob, sys, os

path_cut = sys.argv[1]
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


for f_cut in glob.glob(path_cut+'/*.cut'):
    video = f_cut.split('/')[-1].split('.')[0]
    print video
    if os.path.isfile(path_idx+video+'.MPG.idx'):
        dic_idx = sync_idx(path_idx+'/'+video+'.MPG.idx')
        fout = open(path_out+'/'+video+'.mdtm', 'w')
        l_c = []
        for c in open(f_cut):
            l_c.append(int(c[:-1]))
 
        l_c.sort()
        for i in range(len(l_c)-1):
            l_c[i], l_c[i+1]
            fout.write(video+' 1 '+str(dic_idx[l_c[i]])+' '+str(round(dic_idx[l_c[i+1]] - dic_idx[l_c[i]], 3))+' shot na na shot_'+str(i)+'\n')
        fout.close()
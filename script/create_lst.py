import glob, os, sys

lst_global = sys.argv[1]
REPERE_path = sys.argv[2]

l_video_ok = []
for line in open(lst_global):
    l_video_ok.append(line[:-1])

data_path = {'dev0':['DEV', 'dev0/'],
             'dev2':['DEV', 'dev2/'],
             'test0':['TEST', 'test0/'],
             'test1':['TEST', 'test1/'],
             'test2':['TEST', 'test2/'],
             'train':['TRAIN', '']
             }
l_video_path = []
l_video = []
for s, sub_path in sorted(data_path.items()):
    fout = open(REPERE_path+'/uri_lst/uri.REPERE.'+s+'.lst', 'w')

    path_AUDIO = sub_path[0]+'/AUDIO/'+sub_path[1]
    path_VIDEO = sub_path[0]+'/VIDEO/'+sub_path[1]
    path_TRS = sub_path[0]+'/TRS/'+sub_path[1]
    path_XGTF = sub_path[0]+'/XGTF/'+sub_path[1]
    path_IDX = sub_path[0]+'/IDX/'+sub_path[1]

    for f in glob.glob(REPERE_path+'/DATA/SOURCE DATA/'+path_TRS+'/*'):
        video = f.split('/')[-1].split('.')[0]
        print video
        if video in l_video_ok:
            fout.write(video+'\n')
            l_video_path.append(video+' '+path_AUDIO+video+'.wav '+path_VIDEO+video+'.avi '+path_VIDEO+video+'.MPG '+path_TRS+video+'.trs '+path_XGTF+video+'.xgtf '+path_IDX+video+'.MPG.idx\n')            
            l_video.append(video+'\n')
    fout.close()

fout = open(REPERE_path+'/dataPath.lst', 'w')
for line in sorted(l_video_path):
    fout.write(line)
fout.close()

fout = open(REPERE_path+'/uri_lst/uri.REPERE.all.lst', 'w')
for line in sorted(l_video):
    fout.write(line)
fout.close()






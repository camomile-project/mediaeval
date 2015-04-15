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

for s, sub_path in sorted(data_path.items()):
    fout = open(REPERE_path+'/uri_lst/uri.'+s+'.lst', 'w')

    path_AUDIO = '/DATA/SOURCE DATA/'+sub_path[0]+'/AUDIO/'+sub_path[1]
    path_VIDEO = '/DATA/SOURCE DATA/'+sub_path[0]+'/VIDEO/'+sub_path[1]
    path_TRS = '/DATA/SOURCE DATA/'+sub_path[0]+'/TRS/'+sub_path[1]
    path_XGTF = '/DATA/SOURCE DATA/'+sub_path[0]+'/XGTF/'+sub_path[1]
    path_IDX = '/DATA/SOURCE DATA/'+sub_path[0]+'/IDX/'+sub_path[1]

    for f in glob.glob(REPERE_path+'/'+path_TRS+'/*'):
        video = f.split('/')[-1].split('.')[0]
        if video in l_video_ok:
            fout.write(video)
            fout.write('\t'+path_AUDIO+video+'.wav')
            fout.write('\t'+path_VIDEO+video+'.avi')
            fout.write('\t'+path_VIDEO+video+'.MPG')
            fout.write('\t'+path_TRS+video+'.trs')
            fout.write('\t'+path_XGTF+video+'.xgtf')
            fout.write('\t'+path_IDX+video+'.MPG.idx')
            fout.write('\n')
    fout.close()

fout = open(REPERE_path+'/uri_lst/uri.ALL.lst', 'w')
for s, sub_path in sorted(data_path.items()):
    for line in open(REPERE_path+'/uri_lst/uri.'+s+'.lst'):
        fout.write(line)


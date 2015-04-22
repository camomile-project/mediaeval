import glob, os

lst = 'uri.all.lst'
video_list_file = '/people/poignant/Dev/REPERE/uri_lst/'+lst

array_file = '/people/poignant/Dev/script_qsub/tmp/array_cut_hist_OF_score.sh'
file_out_list  = '/people/poignant/Dev/script_qsub/tmp/list_cut_hist_OF_score'
cde = "python '/people/poignant/Dev/SourceCodeSystem/SubComponent/1_Shot/1_extract_descriptor.py'"

video_path = '/vol/work1/poignant/video_repere_avi/'
video_extension = 'avi'
output_path = '/vol/work1/poignant/MetaData/1_Shot/descriptor/'
idx = '/people/poignant/Dev/REPERE/idx/'

nb_concurrent_jobs = 200

fout_array = open(array_file, 'w')
fout_array.write('#!/bin/bash\n')
fout_array.write('export PYTHONPATH=$PYTHONPATH:/people/poignant/Dev/SourceCodeSystem\n')
fout_array.write(cde+" `head -n $SGE_TASK_ID $1 | tail -n 1` ")
fout_array.close()

nb_file = 0
fout_list = open(file_out_list, 'w')
for video in open(video_list_file).read().splitlines():
    fout_list.write(video_path+'/'+video+'.'+video_extension)
    fout_list.write(" "+output_path+'/'+video+'.desc')
    fout_list.write(" --idx="+idx+'/'+video+'.MPG.idx')
    fout_list.write('\n')
    nb_file+=1
fout_list.close()

os.popen('qsub -S /bin/bash -V -j y -tc '+str(nb_concurrent_jobs)+' -t 1:'+str(nb_file)+' '+array_file+' '+file_out_list)
#os.popen('qsub -S /bin/bash -q 48giga.q -V -j y -tc '+str(nb_concurrent_jobs)+' -t 1:'+str(nb_file)+' '+array_file+' '+file_out_list)




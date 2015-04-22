import glob, os

lst = 'uri.all.lst'
video_list_file = '/people/poignant/Dev/REPERE/uri_lst/'+lst

array_file = '/people/poignant/Dev/script_qsub/tmp/array_face_tracking.sh'
file_out_list  = '/people/poignant/Dev/script_qsub/tmp/list_face_tracking'
cde =  'python /people/poignant/Dev/SourceCodeSystem/SubComponent/3_Face/2_face_tracking.py'

nb_concurrent_jobs=60
nb_file = 0

fout_array = open(array_file, 'w')
fout_array.write('#!/bin/bash\n')
fout_array.write('export PYTHONPATH=$PYTHONPATH:/people/poignant/Dev/SourceCodeSystem\n')
fout_array.write(cde+" `head -n $SGE_TASK_ID $1 | tail -n 1` ")
fout_array.close()

min_duration='2'
video_path = '/vol/work1/poignant/video_repere_avi/'
video_extension = 'avi'
MetaData_path = '/vol/work1/poignant/MetaData/'
idx_path = '/people/poignant/Dev/REPERE/idx/'

fout_list = open(file_out_list, 'w')
for video in open(video_list_file).read().splitlines():
    fout_list.write(" "+video_path+'/'+video+'.'+video_extension)
    fout_list.write(" "+MetaData_path+'/1_Shot/segmentation_uem_'+min_duration+'/'+video+'.shot')
    fout_list.write(" "+MetaData_path+'/3_Face/detection/'+video+'.face')
    fout_list.write(" "+MetaData_path+'/3_Face/tracking/'+video+'.facetrack')
    fout_list.write(" "+MetaData_path+'/3_Face/facetracks_segmentation/'+video+'.seg')
    fout_list.write(" --idx="+idx_path+'/'+video+'.MPG.idx')
    fout_list.write('\n')
    nb_file+=1
fout_list.close()

os.popen('qsub -S /bin/bash -V -j y -tc '+str(nb_concurrent_jobs)+' -t 1:'+str(nb_file)+' '+array_file+' '+file_out_list)
#os.popen('qsub -S /bin/bash -q 48giga.q -V -j y -tc '+str(nb_concurrent_jobs)+' -t 1:'+str(nb_file)+' '+array_file+' '+file_out_list)




import os, sys
import ConfigParser

if __name__ == '__main__':
    process = sys.argv[1]
    corpus = sys.argv[2]
    nb_concurrent_jobs = sys.argv[3]

    l_process_authorized = ['shot_desc', 'shot_seg', 
                            'face_detection', 'face_tracking', 'flandmark', 'face_desc', 'l2_mat', 'face_proba_mat',
                            'speech_seg', 'st_seg', 'linear_BIC_clus', 'BIC_mat', 'st_proba_mat']
    if process not in l_process_authorized:
        print 'process unknown, select a process in:', l_process_authorized
        sys.exit(2)

    Config = ConfigParser.ConfigParser()
    Config.read("config_qsub.ini")
    corpusPath = Config.get('mainSection', 'corpusPath')
    metaData = Config.get('mainSection', 'metaData')
    SourceCodeSystem = Config.get('mainSection', 'SourceCodeSystem')
    mediaevalRepo = Config.get('mainSection', 'mediaevalRepo')

    dataPathlst = metaData+'dataPath.lst'

    dataPath = {}
    for path in open(dataPathlst).read().splitlines():
        videoID, wave_file, video_avi_file, video_mpeg_file, trs_file, xgtf_file, idx_file = path.split(' ')
        dataPath[videoID] = {'wave' : corpusPath+wave_file,
                             'avi' : corpusPath+video_avi_file,
                             'mpeg' : corpusPath+video_mpeg_file,
                             'trs' : corpusPath+trs_file,
                             'xgtf' : corpusPath+xgtf_file,
                             'idx' : corpusPath+idx_file
                            }

    videoID_lst = []
    for videoID in open(metaData+'uri_lst/'+'uri.'+corpus+'.lst').read().splitlines():
        videoID_lst.append(videoID)
    segmentUEM = metaData+'segment.uem'

    shot_desc = mediaevalRepo+'/data/shot_descriptor/'
    shot_seg = metaData+'shotSegmentation/'

    face_detection = metaData+'SubComponent/Face/detection/'
    face_tracking = metaData+'SubComponent/Face/tracking/'
    facetracks_seg = metaData+'SubComponent/Face/facetracks_segmentation/'
    flandmark = metaData+'SubComponent/Face/flandmark/'
    face_l2_mat = metaData+'SubComponent/Face/l2_matrix/'
    face_proba_mat = metaData+'SubComponent/Face/proba_matrix/'

    speech_seg = metaData+'SubComponent/SpeeechTurn/speech_nonspeech_segmentation/'
    st_seg = metaData+'SubComponent/SpeeechTurn/speech_turn_segmentation/'
    linear_BIC_clus = metaData+'SubComponent/SpeeechTurn/linear_BIC_clustering/'
    BIC_matrix = metaData+'SubComponent/SpeeechTurn/BIC_matrix/'
    st_proba_mat = metaData+'SubComponent/SpeeechTurn/proba_matrix/'

    array_file = mediaevalRepo+'script/tmp/array_'+process+'.sh'
    file_out_list  = mediaevalRepo+'script/tmp/list_'+process
    lines = []

    if process == 'shot_desc':
        cde = "python '"+mediaevalRepo+"shot_descriptor.py' "
        for videoID in videoID_lst:
            lines.append(dataPath[videoID]['avi']+" "+shot_desc+videoID+".desc --idx="+dataPath[videoID]['idx'])

    elif process == 'shot_seg':
        cde = "python '"+mediaevalRepo+"shot_segmentation.py' "
        for videoID in videoID_lst:
            lines.append(videoID+" "+shot_desc+videoID+".desc "+shot_seg+videoID+".shot --min_duration=2 --uem="+segmentUEM)

    elif process == 'face_detection':
        cde = "python '"+SourceCodeSystem+"SubComponent/Face/1_face_detection.py' "
        for videoID in videoID_lst:
            lines.append(dataPath[videoID]['avi']+" "+face_detection+videoID+".face "+SourceCodeSystem+"SubComponent/Model/haarcascade_frontalface_default.xml --shot_segmentation="+shot_seg+videoID+'.shot')

    elif process == 'face_tracking':
        cde = "python '"+SourceCodeSystem+"SubComponent/Face/2_face_tracking.py' "
        for videoID in videoID_lst:
            lines.append(dataPath[videoID]['avi']+" "+shot_seg+videoID+".shot "+face_detection+videoID+".face "+face_tracking+videoID+".facetrack "+facetracks_seg+videoID+".seg --idx="+dataPath[videoID]['idx'])

    # elif process == 'flandmark':
    #     cde = "python '"+SourceCodeSystem+"SubComponent/Face/3_extract_flandmark/build/face_landmarks_detection'"


    # elif process == 'face_desc':
    #     cde = "python '"+SourceCodeSystem+"SubComponent/Face/4_face_HoG_descriptor.py' "


    # elif process == 'l2_mat':
    #     cde = "python '"+SourceCodeSystem+"SubComponent/Face/5_compute_hvh_matrix.py' "


    elif process == 'speech_seg':
        cde = "python '"+SourceCodeSystem+"SubComponent/SpeechTurn/2_speech_nonspeech_segmentation.py' "
        for videoID in videoID_lst:
            lines.append(dataPath[videoID]['wave']+" "+SourceCodeSystem+"SubComponent/Model/model_speech_nonspeech_256gauss "+speech_seg+videoID+".mdtm")

    elif process == 'st_seg':
        cde = "python '"+SourceCodeSystem+"SubComponent/SpeechTurn/3_speech_turn_segmentation.py' "
        for videoID in videoID_lst:
            lines.append(videoID+" "+dataPath[videoID]['wave']+" "+speech_seg+videoID+".mdtm "+st_seg+videoID+".mdtm")

    elif process == 'linear_BIC_clus':
        cde = "python '"+SourceCodeSystem+"SubComponent/SpeechTurn/4_linear_bic_clustering.py' "
        for videoID in videoID_lst:
            lines.append(videoID+" "+dataPath[videoID]['wave']+" "+st_seg+videoID+".mdtm "+linear_BIC_clus+videoID+".mdtm")

    elif process == 'BIC_mat':
        cde = "python '"+SourceCodeSystem+"SubComponent/SpeechTurn/.py' "
        for videoID in videoID_lst:
            lines.append(videoID+" "+dataPath[videoID]['wave']+" "+linear_BIC_clus+videoID+".mdtm "+BIC_matrix+videoID+".mat")

    # elif process == 'st_proba_mat':
    #     cde = "python '"+SourceCodeSystem+"SubComponent/SpeechTurn/.py' "




    fout_array = open(array_file, 'w')
    fout_array.write('#!/bin/bash\n')
    fout_array.write('export PYTHONPATH=$PYTHONPATH:/people/poignant/Dev/SourceCodeSystem\n')
    fout_array.write(cde+" `head -n $SGE_TASK_ID $1 | tail -n 1` ")
    fout_array.close()  

    fout_list = open(file_out_list, 'w')
    for line in lines:
        fout_list.write(line+'\n')
    fout_list.close() 

    os.popen('qsub -S /bin/bash -V -j y -tc '+str(nb_concurrent_jobs)+' -t 1:'+str(len(lines))+' '+array_file+' '+file_out_list)




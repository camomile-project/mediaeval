import glob, sys, os
from pyannote.parser import MDTMParser
from pyannote.core import Annotation, Segment

video_list = sys.argv[1]
shot_seg_path = sys.argv[2]
face_seg_path = sys.argv[3]
spk_seg_path = sys.argv[4]
OCR_seg_path = sys.argv[5]
Spoken_seg_path = sys.argv[6]
output_path = sys.argv[7]
marging_spoken = int(sys.argv[8])

for line in open(video_list):
    video = line.split('\t')[0]
    print video

    shots = Annotation(uri=video, modality='shot')
    for line in open(shot_seg_path+'/'+video+'.shot'):
        video, shotID, startTime, endTime, startFrame, endFrame = line[:-1].split(' ')
        segment = Segment(start=float(startTime), end=float(endTime))
        shots[segment] = shotID

    faces = MDTMParser().read(face_seg_path+'/'+video+'.mdtm')(uri=video, modality="head")
    speakers = MDTMParser().read(spk_seg_path+'/'+video+'.mdtm')(uri=video, modality="speaker")

    OCR = Annotation(uri=video, modality='written')
    if os.path.isfile(OCR_seg_path+'/'+video+'.mdtm'):
        OCR = MDTMParser().read(OCR_seg_path+'/'+video+'.mdtm')(uri=video, modality="written")

    spokens = Annotation(uri=video, modality='spoken')
    if os.path.isfile(Spoken_seg_path+'/'+video+'.mdtm'):
        spokens_tmp = MDTMParser().read(Spoken_seg_path+'/'+video+'.mdtm')(uri=video, modality="spoken")
    for seg_spoken in spokens_tmp.get_timeline():
        segment = Segment(start=float(seg_spoken.start-marging_spoken), end=float(seg_spoken.end+marging_spoken))
        for spoken in spokens_tmp.get_labels(seg_spoken):
            spokens[segment] = spoken

    fout = open(output_path+'/'+video+'.shot', 'w')
    for seg_shot in shots.get_timeline():
        shot = list(shots.get_labels(seg_shot))[0]
        l_spk = set([])
        l_face = set([])
        for seg_spk in speakers.get_timeline():
            if seg_shot & seg_spk:
                for spk in speakers.get_labels(seg_spk):
                    l_spk.add(spk)

        for seg_face in faces.get_timeline():
            if seg_shot & seg_face:
                for face in faces.get_labels(seg_face):
                    l_face.add(face)

        for name in l_spk & l_face:
            if 'BFMTV_' not in name and 'LCP_' not in name:
                evidence = 'false'
                for seg_ocr in OCR.get_timeline():
                    if seg_shot & seg_ocr:
                        for ocr in OCR.get_labels(seg_ocr):
                            if ocr == name :
                                evidence = 'true_ocr'

                for seg_spoken in spokens.get_timeline():
                    if seg_shot & seg_spoken:
                        for spoken in spokens.get_labels(seg_spoken):
                            if spoken == name :
                                if evidence:
                                    evidence += '_asr'
                                else:
                                    evidence = 'true_asr'

                fout.write(video+' '+shot+' '+name+' '+evidence+'\n')

    fout.close()

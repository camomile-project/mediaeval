import glob, sys, os
from pyannote.parser import MDTMParser
from pyannote.core import Annotation, Segment

uri_lst = sys.argv[1]
shot_seg_path = sys.argv[2]
face_seg_path = sys.argv[3]
spk_seg_path = sys.argv[4]
OCR_seg_path = sys.argv[5]
Spoken_seg_path = sys.argv[6]
output_path = sys.argv[7]
marging_spoken = int(sys.argv[8])

def parser_vtseg(f, video):
    anno = Annotation(uri=video)
    for line in open(f):
        video, startTime, endTime, startFrame, endFrame, name = line[:-1].split(' ')
        segment = Segment(start=float(startTime), end=float(endTime))
        anno[segment] = name
    return anno

def parser_atseg(f, video):
    anno = Annotation(uri=video)
    for line in open(f):
        video, startTime, endTime, name = line[:-1].split(' ')
        segment = Segment(start=float(startTime), end=float(endTime))
        anno[segment] = name
    return anno

for video in open(uri_lst).read().splitlines():
    print video

    shots = Annotation(uri=video, modality='shot')
    for line in open(shot_seg_path+'/'+video+'.shot'):
        video, shotID, startTime, endTime, startFrame, endFrame = line[:-1].split(' ')
        segment = Segment(start=float(startTime), end=float(endTime))
        shots[segment] = shotID

    faces = parser_vtseg(face_seg_path+'/'+video+'.vtseg', video)
    speakers = parser_atseg(spk_seg_path+'/'+video+'.atseg', video)

    OCR = Annotation(uri=video, modality='written')
    if os.path.isfile(OCR_seg_path+'/'+video+'.vtseg'):
        OCR = parser_vtseg(OCR_seg_path+'/'+video+'.vtseg', video)

    spokens = Annotation(uri=video, modality='spoken')
    if os.path.isfile(Spoken_seg_path+'/'+video+'.atseg'):
        spokens_tmp = parser_atseg(Spoken_seg_path+'/'+video+'.atseg', video)

        for seg_spoken in spokens_tmp.get_timeline():
            segment = Segment(start=float(seg_spoken.start-marging_spoken), end=float(seg_spoken.end+marging_spoken))
            for spoken in spokens_tmp.get_labels(seg_spoken):
                spokens[segment] = spoken

    fout = open(output_path+'/'+video+'.ref', 'w')
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
                evidenceSource = 'na'
                for seg_ocr in OCR.get_timeline():
                    if seg_shot & seg_ocr:
                        for ocr in OCR.get_labels(seg_ocr):
                            if ocr == name :
                                evidence = 'true'
                                evidenceSource = 'image'

                for seg_spoken in spokens.get_timeline():
                    if seg_shot & seg_spoken:
                        for spoken in spokens.get_labels(seg_spoken):
                            if spoken == name :
                                if evidence == 'true':
                                    evidenceSource = 'both'
                                else:
                                    evidence = 'true'
                                    evidenceSource = 'audio'

                fout.write(video+' '+shot+' '+name+' '+evidence+' '+evidenceSource+'\n')

    fout.close()

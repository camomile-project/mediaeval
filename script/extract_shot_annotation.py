import glob, sys
from pyannote.parser import MDTMParser
from pyannote.core import Annotation, Segment

video_list = sys.argv[1]
shot_seg_path = sys.argv[2]
face_seg_path = sys.argv[3]
spk_seg_path = sys.argv[4]
output_path = sys.argv[5]

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
            fout.write(video+' '+shot+' '+name+' ?\n')

    fout.close()

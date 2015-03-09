import glob, sys
from pyannote.parser import MDTMParser
from pyannote.core import Annotation

list_video = sys.argv[1]
path_shot = sys.argv[2]
path_face_seg = sys.argv[3]
path_spk_seg = sys.argv[4]
path_out = sys.argv[5]


for line in open(list_video):
    video = line[:-1]
    print video
    shots = MDTMParser().read(path_shot+'/'+video+'.mdtm')(uri=video, modality="shot")
    faces = MDTMParser().read(path_face_seg+'/'+video+'.mdtm')(uri=video, modality="head")
    speakers = MDTMParser().read(path_spk_seg+'/'+video+'.mdtm')(uri=video, modality="speaker")

    fout = open(path_out+'/'+video+'.shot_person', 'w')
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
            fout.write(shot+' '+name+'\n')

    fout.close()

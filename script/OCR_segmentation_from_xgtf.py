from xml.dom import minidom
from repere import IDXHack
import unicodedata
import sys, os

uri_lst = sys.argv[1]
REPERE_path = sys.argv[2]
output_path_seg = sys.argv[3]

for path in open(uri_lst).read().splitlines():
    video, wave_file, video_avi_file, video_mpeg_file, trs_file, xgtf_file, idx_file = path.split(' ')
    print video

    frame2time = IDXHack(REPERE_path+'/'+idx_file)
    l_ocr = []
    xgtf = minidom.parse(REPERE_path+'/'+xgtf_file)
    for obj in xgtf.getElementsByTagName('object'):
        if obj.getAttribute('name') == 'TEXTE':
            name ='?'
            startFrame = '?'
            endFrame = '?'
            cartouche = 'false'
            framespan = obj.getAttribute('framespan')
            for att in obj.getElementsByTagName('attribute'):
                if att.getAttribute('name') == 'CARTOUCHE':
                    if len(att.getElementsByTagName('data:bvalue')) != 0:
                        cartouche = att.getElementsByTagName('data:bvalue')[0].getAttribute('value')
                if att.getAttribute('name') == 'TRANSCRIPTION':
                    if len(att.getElementsByTagName('data:svalue')) != 0:
                        texte = att.getElementsByTagName('data:svalue')[0].getAttribute('value')
                        if '<pers=' in texte[:6] and '</pers>' in texte:
                            name = texte.split('<pers=')[1].split('>')[0]
                            if isinstance(name,str):
                                name = unicode(name,"utf8","replace")
                            name=unicodedata.normalize('NFD',name)
                            name=name.encode('ascii','ignore') 
                if att.getAttribute('name') == 'STARTFRAME':
                    if len(att.getElementsByTagName('data:dvalue')) != 0:
                        startFrame = att.getElementsByTagName('data:dvalue')[0].getAttribute('value')

                if att.getAttribute('name') == 'ENDFRAME':
                    if len(att.getElementsByTagName('data:dvalue')) != 0:
                        endFrame = att.getElementsByTagName('data:dvalue')[0].getAttribute('value')

            if cartouche == 'true':
                startTime = frame2time(int(startFrame), -1.0)
                endTime = frame2time(int(endFrame), -1.0)
                l_ocr.append([video, startFrame, endFrame, startTime, endTime, name.lower().replace('-', '_')])

    if l_ocr != []:
        fout_seg = open(output_path_seg+'/'+video+'.vtseg','w')
        for video, startFrame, endFrame, startTime, endTime, name in l_ocr:
            fout_seg.write(video)
            fout_seg.write(' %09.3f %09.3f' % (startTime, endTime))
            fout_seg.write(' %07d %07d' % (int(startFrame), int(endFrame)))
            fout_seg.write(' '+name.lower().replace('-', '_'))
            fout_seg.write('\n')
        fout_seg.close()


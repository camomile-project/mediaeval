from xml.dom import minidom
from repere import IDXHack
import unicodedata
import sys, os

uri_lst = sys.argv[1]
REPERE_path = sys.argv[2]
output_path_seg = sys.argv[3]
output_path_position = sys.argv[4]

for path in open(uri_lst).read().splitlines():
    video, wave_file, video_avi_file, video_mpeg_file, trs_file, xgtf_file, idx_file = path.split('\t')

    print video

    frame2time = IDXHack(REPERE_path+'/'+idx_file)
    fout_position = open(output_path_position+'/'+video+'.position','w')
    fout_seg = open(output_path_seg+'/'+video+'.mdtm','w')
    xgtf = minidom.parse(REPERE_path+'/'+xgtf_file)
    for obj in xgtf.getElementsByTagName('object'):
        if obj.getAttribute('name') == 'PERSONNE':
            name ='?'
            l_pts = []
            start = '?'
            end = '?'
            role = '?'
            framespan = obj.getAttribute('framespan')
            for att in obj.getElementsByTagName('attribute'):
                if att.getAttribute('name') == 'NOM':
                    if len(att.getElementsByTagName('data:svalue')) != 0:
                        name = att.getElementsByTagName('data:svalue')[0].getAttribute('value')
                        if isinstance(name,str):
                            name = unicode(name,"utf8","replace")
                        name=unicodedata.normalize('NFD',name)
                        name=name.encode('ascii','ignore') 
                if att.getAttribute('name') == 'TETE':
                    if len(att.getElementsByTagName('data:polygon')) != 0:
                        for pts in att.getElementsByTagName('data:polygon')[0].getElementsByTagName('data:point'):
                            l_pts.append([int(pts.getAttribute('x')), int(pts.getAttribute('y'))])

                if att.getAttribute('name') == 'STARTFRAME':
                    if len(att.getElementsByTagName('data:dvalue')) != 0:
                        start = att.getElementsByTagName('data:dvalue')[0].getAttribute('value')

                if att.getAttribute('name') == 'ENDFRAME':
                    if len(att.getElementsByTagName('data:dvalue')) != 0:
                        end = att.getElementsByTagName('data:dvalue')[0].getAttribute('value')

                if att.getAttribute('name') == 'ROLE':
                    if len(att.getElementsByTagName('data:lvalue')) != 0:
                        role = att.getElementsByTagName('data:lvalue')[0].getAttribute('value')

            fout_position.write(start+' '+end+' '+framespan.split(':')[0]+' '+name+' '+role+' ')
            if l_pts == []:
                fout_position.write('?:?')
            else:
                fout_position.write(str(l_pts[0][0])+':'+str(l_pts[0][1]))
                for pt in l_pts[1:]:
                    fout_position.write(';'+str(pt[0])+':'+str(pt[1]))            
            fout_position.write('\n')

            startTime = frame2time(int(start), -1.0)
            endTime = frame2time(int(end), -1.0)
            fout_seg.write(video+' 1 '+str(startTime)+' '+str(endTime-startTime)+' head na na '+name+'\n')

    fout_position.close()
    fout_seg.close()


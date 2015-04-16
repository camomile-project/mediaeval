from xml.dom import minidom
import unicodedata, os, sys

uri_lst = sys.argv[1]
REPERE_path = sys.argv[2]
output_path_seg = sys.argv[3]

for path in open(uri_lst).read().splitlines():
    video, wave_file, video_avi_file, video_mpeg_file, trs_file, xgtf_file, idx_file = path.split(' ')

    print wave_file

    fout_seg = open(output_path_seg+'/'+video+'.atseg','w')
    trs = minidom.parse(REPERE_path+'/'+trs_file)

    tag_to_name = {}
    for spk in trs.getElementsByTagName('Speaker'):
        name = spk.getAttribute('name')
        if isinstance(name,str):
            name = unicode(name,"utf8","replace")
        name=unicodedata.normalize('NFD',name)
        name=name.encode('ascii','ignore')  
        tag_to_name[spk.getAttribute('id')] = name

    for turn in trs.getElementsByTagName('Turn'):
        startTime = float(turn.getAttribute('startTime'))
        endTime = float(turn.getAttribute('endTime'))
        spks = turn.getAttribute('speaker')
        if spks != '':
            for spk in spks.split(' '):
                fout_seg.write(video)
                fout_seg.write(' %09.3f %09.3f' % (startTime, endTime))
                fout_seg.write(' '+tag_to_name[spk].lower().replace('-', '_'))
                fout_seg.write('\n')
    fout_seg.close()


import sys

spokenref_file = sys.argv[1]
output_path_seg = sys.argv[2]


dic = {}
for line in open(spokenref_file):
    video, startTime, endTime, spoken, name = line[:-1].split(' ')
    dic.setdefault(video, []).append([float(startTime), float(endTime), name.lower().replace('-', '_')])

for video in sorted(dic):
    fout_seg = open(output_path_seg+'/'+video+'.atseg', 'w')
    for startTime, endTime, name in sorted(dic[video]):
        fout_seg.write(video)
        fout_seg.write(' %09.3f %09.3f' % (startTime, endTime))
        fout_seg.write(' '+name)
        fout_seg.write('\n')
    fout_seg.close()
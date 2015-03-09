import glob, sys

path_trs = sys.argv[1]
path_out = sys.argv[2]

def trs_parser(f_trs):
    d_spk = {}
    seg = []
    for line in open(f_trs):
        if '<Speaker id="' in line:
            name = line.split('name="')[1].split('"')[0]
            Id = line.split('id="')[1].split('"')[0]
            d_spk[Id] = name

        if '<Turn ' in line and 'speaker="' in line:
            s = float(line.split('startTime="')[1].split('"')[0])
            e = float(line.split('endTime="')[1].split('"')[0])
            for Id in line.split('speaker="')[1].split('"')[0].split(' '):
                seg.append([s, e, d_spk[Id]])
    return seg

for f_trs in glob.glob(path_trs+'/*.trs'):
    video = f_trs.split('/')[-1].split('.')[0]
    print video
    seg = trs_parser(f_trs)

    fout = open(path_out+'/'+video+'.mdtm', 'w')
    for s, e, name in sorted(seg):
        fout.write(video+' 1 '+str(s)+' '+str(round(e-s, 3))+' speaker na na '+name+'\n')
    fout.close()
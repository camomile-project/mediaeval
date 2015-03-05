"""
Eval MMAP

Usage:
  eval_MMAP.py <path_file_rank> <file_ref> <file_list_query_ranking> <size_rank>
  eval_MMAP.py -h | --help
"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    path_file_rank = arguments['<path_file_rank>']
    file_ref = arguments['<file_ref>']
    file_list_query_ranking = arguments['<file_list_query_ranking>']
    size_rank = int(arguments['<size_rank>'])

    l_file_query_per_name = {}
    for line in open(file_list_query_ranking):
        name, start_date, end_date, file_rank = line.split(' ')
        l_file_query_per_name.setdefault(name, []).append(file_rank)

    dic_ref = {}
    for line in open(file_ref):
        video, name, shot = line[:-1]
        dic_ref.setdefault(name, {})
        dic_ref[name].setdefault(video, []).append(shot)

    MMAP = 0.0
    for name in l_file_query_per_name:
        MAP = 0.0
        for f in l_file_query_per_name[name]:
            AP = 0.0
            rank = 0.0
            nb_cor = 0.0
            for line in open(f)
                video, shot, conf = line[:-1].split(' ')
                rank += 1
                if video in dic_ref[name]:
                    if shot in dic_ref[name][video]:
                        nb_cor+=1.0
                        AP += nb_cor/rank
                if rank>size_rank:
                    break
            AP/=nb_cor 
            MAP += AP
        MAP /= len(l_file_query_per_name[name])
        print 'MAP for:', name, MAP
        MMAP += MAP
    MMAP /= len(l_file_query_per_name)
    print 'total MMAP:', MMAP





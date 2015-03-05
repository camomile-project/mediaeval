"""
Rank shot indexed for a query(JOHN_SMITH, 17/01/2015, 27/01/2015)

Usage:
  rank_shot.py <q_name> <q_start_date> <q_end_date> <file_shot_indexed> <output_file> [--Levenshtein_ratio=<lr>] 
  rank_shot.py -h | --help
Options:
  --Levenshtein_ratio=<lr>   threshold on the Levenshtein ratio between the query name and the name in the indexation [default: 0.9]
"""

from docopt import docopt
import datetime
import Levenshtein

if __name__ == '__main__':
    arguments = docopt(__doc__)
    q_name = arguments['<q_name>']
    q_start_date = datetime.datetime.strptime(arguments['<q_start_date>'], "%d/%m/%Y").date()
    q_end_date = datetime.datetime.strptime(arguments['<q_end_date>'], "%d/%m/%Y").date()
    file_shot_indexed = arguments['<file_shot_indexed>']
    output_file = arguments['<output_file>']
    Levenshtein_ratio = float(arguments['<Levenshtein_ratio>'])

    l_shot = []
    for line in open(file_shot_indexed):
        video, date, shot, name, confidence = line[:-1].split(' ')    
        date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
        if date >= q_start_date and date <= q_end_date and Levenshtein.ratio(name, q_name)>Levenshtein_ratio :
            confidence = float(confidence)
            l_shot.append(confidence, video, shot)

    l_shot.sort(reverse = True)
    fout = open(output_file, 'w')
    for conf, video, shot in l_shot:
        fout.write(video+' '+shot+' '+str(conf)+'\n')
    fout.close()

"""
extract images for each shot

Usage:
  segmentation.py <video_file> <shot_seg> <outputPath>
  segmentation.py -h | --help
"""

from docopt import docopt
import cv2, cv

if __name__ == '__main__':
    # read arguments
    args = docopt(__doc__)

    l_image_to_save = {}
    for line in open(args['<shot_seg>']).read().splitlines():
        videoID, shotID, startTime, endTime, startFrame, endFrame = line.split(' ')
        l_image_to_save[int(startFrame)] = [args['<outputPath>']+'/'+shotID+'_'+startTime+'.jpg']
        l_image_to_save[int(endFrame)] = [args['<outputPath>']+'/'+shotID+'_'+endTime+'.jpg']

    capture = cv2.VideoCapture(args['<video_file>'])
    nb_frame = int(capture.get(cv.CV_CAP_PROP_FRAME_COUNT))
    c_frame = 0
    while (c_frame<nb_frame):
        ret, frame = capture.read()
        c_frame = int(capture.get(cv.CV_CAP_PROP_POS_FRAMES))
        if ret and c_frame in l_image_to_save:
            cv2.imwrite(l_image_to_save[c_frame], frame)

#!/usr/bin/env python3
"""
This script takes as input a directory which stores images to be selected.
This script outputs a directory named as "[input dir]_bbox" in the current working directory.
A {label}_bbox.csv file is written in the output directory with the following columns:
['file','x1','y1','x2','y2','label']
where 'file' is the filename (with absolute path), 'x1', 'y1' is the top left coordinate and 'x2', 'y2' is the bottom right coordinate of the selected ROI.

It is suggested to run this script for one interested subject, then add a last column to the above file with the label for said subject.
Repeat for a different subject.  Then concatenate all csv files to a main csv.
"""

import numpy as np
import pandas as pd
import os, glob, re
import argparse
import cv2
import gc

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, type=str, help="path to input directory of images")
args = ap.parse_args()

CURDIR = os.path.abspath(os.path.curdir)
DATASET = os.path.abspath(args.dataset)
OUTDIR = os.path.join(CURDIR, os.path.split(DATASET)[1] + '_bbox')

if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)

files = glob.glob(f'{DATASET}/**/*', recursive=True)
regex = re.compile(r'.*\.(jpe?g|png|tiff?|bmp)', flags=re.I)
images = list(filter(regex.search, files))
images.sort()

print(args)
print(OUTDIR, '\n')

df = pd.DataFrame(columns=['file','x1','y1','x2','y2'])

for (i, image) in enumerate(images, start=1):
    print('Processing image', os.path.relpath(image), f' ({i} / {len(images)})\n')
    try:
        img = cv2.imread(image)
        bbox = cv2.selectROIs('bbox', img, showCrosshair=False, fromCenter=False)
    except Exception as exc:
        print(exc)
        continue
    if len(bbox) == 0:
        continue
    im = np.empty([bbox.shape[0],1], dtype=object)
    im[:] = image
    df = df.append(pd.DataFrame(np.c_[im, bbox], columns=['file','x1','y1','x2','y2']), ignore_index=True)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#cv2.selectROIs returns x,y and w,h; the below is to convert to x1,y1 and x2,y2
df.loc[:,'x2'] = df.loc[:,'x1'] + df.loc[:,'x2']
df.loc[:,'y2'] = df.loc[:,'y1'] + df.loc[:,'y2']

print('\nInput the label of the selected class\n')
label = input()
df['label'] = label

print(df)
print('Output to: ' + os.path.join(os.path.relpath(OUTDIR), f'{label.replace(" ","_")}_bbox.csv'))
df.to_csv(os.path.join(OUTDIR, f'{label.replace(" ","_")}_bbox.csv'), index=False, header=True)

try:
    del(im,img,image,images,df,i,CURDIR,OUTDIR,DATASET,ap,args,files,regex,bbox,label)
except:
    pass

gc.collect()

import numpy as np
import pandas as pd
import os, glob, re
import argparse
import cv2
import gc

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True, type=str, help="path to input csv of ROI's")
args = ap.parse_args()

CURDIR = os.path.abspath(os.path.curdir)
DATASET = os.path.abspath(args.dataset)
OUTDIR = os.path.split(DATASET)[0]

df = pd.read_table(DATASET, sep=',')
print(args)
print(OUTDIR)

for i in df.index:
    name = df.loc[i, 'file']
    print('Processing image', f' {name} ({i+1} / {df.shape[0]})')
    try:
        img = cv2.imread(name)
    except Exception as exc:
        print(exc)
        continue
    x1 = df.loc[i, 'x1']
    y1 = df.loc[i, 'y1']
    x2 = df.loc[i, 'x2']
    y2 = df.loc[i, 'y2']
    roi_img = img[y1:y2, x1:x2]

    extracted_name, _, extracted_extension = os.path.split(name)[1].partition('.')
    roi_name = f'{extracted_name}_{x1}_{y1}_{x2}_{y2}.{extracted_extension}'
    print(f'Output ROI to {os.path.join(OUTDIR, roi_name)}\n')
    cv2.imwrite(os.path.join(OUTDIR, roi_name), roi_img) 
    cv2.imshow('roi', roi_img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        continue

cv2.destroyAllWindows()
try:
    del(name,roi_img,extracted_name,extracted_extension,roi_name,img,df,i,CURDIR,OUTDIR,DATASET,ap,args,x1,x2,y1,y2)
except:
    pass

gc.collect()

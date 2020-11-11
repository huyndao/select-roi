# **`select_roi.py`** and **`extract_roi.py`**

## Description
**`select_roi.py`** will select multiple ROI's (Regions of Interest) per image in a directory.  After finishing selection, the script will ask for a classification name for the selected ROI.  The script will then save the selected ROI's to a csv file in directory `[DIR]_bbox/[CLASS]_bbox.csv`.

**`extract_roi.py`** can then be run on this `[DIR]_bbox/[CLASS]_bbox.csv` file and output images cropped to the ROI's new bounding boxes.  The images will be saved as `[DIR]_bbox/[CLASS]_filename_[X1]_[Y1]_[X2]_[Y2].extension`.

The images can now be used for training in neural networks.

## Install Dependencies
```shell
pip install -r requirements.txt
```
## Requirements
- numpy
- pandas
- opencv-contrib-python

## Help
### select\_roi.py
```shell
python3 select_roi.py -h

usage: select_roi.py [-h] -i DATASET

optional arguments:
  -h, --help            show this help message and exit
  -i DATASET, --dataset DATASET
                        path to input directory of images
```

### extract\_roi.py
```shell
python3 extract_roi.py -h

usage: extract_roi.py [-h] -i DATASET

optional arguments:
  -h, --help            show this help message and exit
  -i DATASET, --dataset DATASET
                        path to input csv of ROI's
```

## Sample Usage
### select\_roi.py
```shell
python3 select_roi.py -i ~/wallpapers/apod/

Namespace(dataset='/home/USER/wallpapers/apod/')
/home/USER/ml/select-roi/apod_bbox 

Processing image ../../wallpapers/apod/00mbcy89pyu51.jpg  (1 / 288)

Finish the selection process by pressing ESC button!
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Processing image ../../wallpapers/apod/04d1b0f960568ab49f36befff9282397.jpg  (2 / 288)
...

Finish the selection process by pressing ESC button!
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
Processing image ../../wallpapers/apod/wr124_hubbleschmidt_1289.jpg  (288 / 288)

Input the label of the selected class

test
                                                file    x1   y1    x2    y2 label
0  /home/USER/wallpapers/apod/04d1b0f960568ab49f...   491  225  1587   803  test
1  /home/USER/wallpapers/apod/JupiterClouds_Juno...   623  558  1472  1282  test
2  /home/USER/wallpapers/apod/JupiterClouds_Juno...  1582  880  1984  1439  test
3  /home/USER/wallpapers/apod/JupiterComplex_Jun...   306  209  1532   991  test
4  /home/USER/wallpapers/apod/N6188_Cappelletti_...   935  421  1800  1196  test
Output to: apod_bbox/test_bbox.csv
```

```shell
cat apod_bbox/test_bbox.csv 

file,x1,y1,x2,y2,label
/home/USER/wallpapers/apod/04d1b0f960568ab49f36befff9282397.jpg,491,225,1587,803,test
/home/USER/wallpapers/apod/JupiterClouds_JunoGill_2295.jpg,623,558,1472,1282,test
/home/USER/wallpapers/apod/JupiterClouds_JunoGill_2295.jpg,1582,880,1984,1439,test
/home/USER/wallpapers/apod/JupiterComplex_JunoMarriott_2324.jpg,306,209,1532,991,test
/home/USER/wallpapers/apod/N6188_Cappelletti_4508.jpg,935,421,1800,1196,test
```

### extract\_roi.py
```shell
python3 extract_roi.py -i apod_bbox/test_bbox.csv 

Namespace(dataset='apod_bbox/test_bbox.csv')
/home/USER/ml/select-roi/apod_bbox
Processing image  /home/USER/wallpapers/apod/04d1b0f960568ab49f36befff9282397.jpg (1 / 5)
Output ROI to /home/USER/ml/select-roi/apod_bbox/test_04d1b0f960568ab49f36befff9282397_491_225_1587_803.jpg

Processing image  /home/USER/wallpapers/apod/JupiterClouds_JunoGill_2295.jpg (2 / 5)
Output ROI to /home/USER/ml/select-roi/apod_bbox/test_JupiterClouds_JunoGill_2295_623_558_1472_1282.jpg

Processing image  /home/USER/wallpapers/apod/JupiterClouds_JunoGill_2295.jpg (3 / 5)
Output ROI to /home/USER/ml/select-roi/apod_bbox/test_JupiterClouds_JunoGill_2295_1582_880_1984_1439.jpg

Processing image  /home/USER/wallpapers/apod/JupiterComplex_JunoMarriott_2324.jpg (4 / 5)
Output ROI to /home/USER/ml/select-roi/apod_bbox/test_JupiterComplex_JunoMarriott_2324_306_209_1532_991.jpg

Processing image  /home/USER/wallpapers/apod/N6188_Cappelletti_4508.jpg (5 / 5)
Output ROI to /home/USER/ml/select-roi/apod_bbox/test_N6188_Cappelletti_4508_935_421_1800_1196.jpg
```

```shell
ls -la apod_bbox/

total 1104
drwxr-xr-x 2 USER USER   4096 Nov 11 16:53 .
drwxr-xr-x 4 USER USER   4096 Nov 11 16:48 ..
-rw-r--r-- 1 USER USER 276600 Nov 11 16:53 test_04d1b0f960568ab49f36befff9282397_491_225_1587_803.jpg
-rw-r--r-- 1 USER USER    442 Nov 11 16:47 test_bbox.csv
-rw-r--r-- 1 USER USER  64661 Nov 11 16:53 test_JupiterClouds_JunoGill_2295_1582_880_1984_1439.jpg
-rw-r--r-- 1 USER USER 207622 Nov 11 16:53 test_JupiterClouds_JunoGill_2295_623_558_1472_1282.jpg
-rw-r--r-- 1 USER USER 393570 Nov 11 16:53 test_JupiterComplex_JunoMarriott_2324_306_209_1532_991.jpg
-rw-r--r-- 1 USER USER 167642 Nov 11 16:53 test_N6188_Cappelletti_4508_935_421_1800_1196.jpg
```

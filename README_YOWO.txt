files:

video_preprocessing_functions.py: contains functions to pre-process Agot data and convert such that it can be into YOWO

Video_Preprocessing.py: main file to pre-process Agot data

build_list_v2.ipynb: Builds test and training list






------------------------------------


SETTING UP YOWO:

YOWO

FOR UCF DATASET:

For Training
1. Download ucf dataset, unzip file. Rename the datafolder as ‘ucf24’.
2. Create a new folder by the name of ‘datasets’. Put the above renamed ‘ucf24’ folder inside the datasets folder.
3.  Download code from GitHub page. The code folder is called YOWO
4. Open cfg/ucf24.data’ in the YOWO folder.  Update address of the base, training and validation dataset
5. Download ‘trainlist.txt’ and ‘testlist.txt’ files and put it inside the ‘ucf24’ folder created in step-1.
6. Create a folder called ‘weights’ in the YOWO folder. 
7. Download pre-trained yolo weights, details given the GitHub page, and put it in the folder created in step-6.
8. Download ‘resnext-101-kinetics.pth’ from the GitHub page and put in the ‘weights’ folder created in step -6.


For Validation
1. Go to YOWO/evaluations/Object-Detection-Metrics
2. unzip the file ‘groundtruths_ucf.zip’
3. Go back to the YOWO folder. Create a folder called ‘ucf_detections/detections_0’. Keep creating multiple subdirectories ‘detections_n’ for n = 0,1,2,3….. for further tasks.
4. Run validation using the command 

Run both training and validating model using the script:
$ sh run_ucf101-24.sh

5. Change the ‘detection_n’ portion in the script file for multiple validation tasks.
python ./evaluation/Object-Detection-Metrics/pascalvoc.py --gtfolder groundtruths_ucf --detfolder ../../ucf_detections/detections_0






------------------------------















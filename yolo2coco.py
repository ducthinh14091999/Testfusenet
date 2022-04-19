# import os
# import json
# import cv2
# import random
# import time
# # (OPTIONAL) step
# # Preparing the Dataset
# # Convert all images to .jpg (This is not necessary but made my life easier down the line)

# from PIL import Image
# #iml = Image.open(r'/absolute/path/to/the/image/directory/followed/by/image/name/with/its/extesnion')
# #rgb_im = iml.convert('RGB')
# #rgb_im.save(r'/absolutae/path/to/the/directory/where/image/must/be/stored/image_name.jpg')
# # (OPTIONAL) step
# # Preparing the Dataset - remove unlabelled files
# # I chose to remove the image files from the dataset that were not labelled
# # Move the files (jpg and txt that are not labelled) from the working directory and put them in another folder. . .

# import shutil

# directory_labels = os.fsencode("/absolute/path/to/labelled/files") #absolute path to the directory where all labels are stored
# directory_images = os.fsencode("/absolute/path/to/images/files") #absolute path to the directory where all images are stored
# directory_unlabelled_images = os.fsencode("/absolute/path/to/newFolder")#absolute path to the directory where unlabelled images are to be stored

# not_labelled_files = 0
# for file in os.listdir(directory_labels): #Read from the directory where the labels are stored
#      filename = os.fsdecode(file)
#      if filename.endswith(".txt"):
#         yolo_annotation_path = (os.path.join(directory_labels.decode("utf-8"), filename))
#         base=os.path.basename(yolo_annotation_path)
#         file_name_without_ext = os.path.splitext(base)[0] # name of the file without the extension
#         img_path = os.path.join(directory_images.decode("utf-8"), file_name_without_ext+ "." + 'jpg')
        
#         filesize = os.path.getsize(yolo_annotation_path)
#         if filesize == 0: #chek if the label file (.txt) is empty - that is it has no labels
#             UnlabeledImg_path = os.path.join(directory_unlabelled_images.decode("utf-8"), file_name_without_ext+ "." + 'jpg')
#             not_labelled_files = not_labelled_files +1
            
#             shutil.move(img_path, UnlabeledImg_path) #remove the corresponding image to another directory
# print("The number of unlabelled files is: ", not_labelled_files)
# #### This is where the conversion process starts from YOLO to COCO format

# # Category file, one category per line
# yolo_format_classes_path = '/media/jyoti/My Passport/DoorDetectDataset/obj.names'
# # Write the category according to your own data set. 

# #Read the categories file and extract all categories
# with open(yolo_format_classes_path,'r') as f1:
#     lines1 = f1.readlines()
# categories = []
# for j,label in enumerate(lines1):
#     label = label.strip()
#     categories.append({'id':j+1,'name':label,'supercategory': label})
    
# write_json_context = dict()
# write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': 2021 , 'contributor': '', 'date_created': '2021-02-12 11:00:08.5'}
# write_json_context['licenses'] = [{'id': 1, 'name': None, 'url': None}]
# write_json_context['categories'] = categories
# write_json_context['images'] = []
# write_json_context['annotations'] = []




# # Read the YOLO formatted label files (.txt) to extarct bounding box information and store in COCO format

# #Read the label files (.txt) to extarct bounding box information and store in COCO format
# directory_labels = os.fsencode("/home/jyoti/Desktop/csc8800/datasets/DoorDetectDataset/labels")
# #directory_images = os.fsencode("/home/jyoti/Desktop/csc8800/datasets/DoorDetectDataset/test")
# directory_images = os.fsencode("/home/jyoti/Desktop/csc8800/datasets/DoorDetectDataset/train")

# file_number = 1
# num_bboxes = 1
# for file in os.listdir(directory_images):
#     filename = os.fsdecode(file)
#     if filename.endswith(".jpg"):
#         img_path = (os.path.join(directory_images.decode("utf-8"), filename))
#         base=os.path.basename(img_path)
#         file_name_without_ext = os.path.splitext(base)[0] # name of the file without the extension
#         yolo_annotation_path  = os.path.join(directory_labels.decode("utf-8"), file_name_without_ext+ "." + 'txt')
#         img_name = os.path.basename(img_path) # name of the file without the extension
#         img_context = {}
#         height,width = cv2.imread(img_path).shape[:2]
#         img_context['file_name'] = img_name
#         img_context['height'] = height
#         img_context['width'] = width
#         img_context['date_captured'] = '2021-02-12 11:00:08.5'
#         img_context['id'] = file_number # image id
#         img_context['license'] = 1
#         img_context['coco_url'] =''
#         img_context['flickr_url'] = ''
#         write_json_context['images'].append(img_context)
        
#         with open(yolo_annotation_path,'r') as f2:
#             lines2 = f2.readlines() 

#         for i,line in enumerate(lines2): # for loop runs for number of annotations labelled in an image
#             line = line.split(' ')
#             bbox_dict = {}
#             class_id, x_yolo,y_yolo,width_yolo,height_yolo= line[0:]
#             x_yolo,y_yolo,width_yolo,height_yolo,class_id= float(x_yolo),float(y_yolo),float(width_yolo),float(height_yolo),int(class_id)
#             bbox_dict['id'] = num_bboxes
#             bbox_dict['image_id'] = file_number
#             bbox_dict['category_id'] = class_id+1
#             bbox_dict['iscrowd'] = 0 # There is an explanation before
#             h,w = abs(height_yolo*height),abs(width_yolo*width)
#             bbox_dict['area']  = h * w
#             x_coco = round(x_yolo*width -(w/2))
#             y_coco = round(y_yolo*height -(h/2))
#             if x_coco <0: #check if x_coco extends out of the image boundaries
#                 x_coco = 1
#             if y_coco <0: #check if y_coco extends out of the image boundaries
#                 y_coco = 1
#             bbox_dict['bbox'] = [x_coco,y_coco,w,h]
#             bbox_dict['segmentation'] = [[x_coco,y_coco,x_coco+w,y_coco, x_coco+w, y_coco+h, x_coco, y_coco+h]]
#             write_json_context['annotations'].append(bbox_dict)
#             num_bboxes+=1
        
#         file_number = file_number+1
#         continue
#     else:
#         continue
        
 # Finally done, save!
#coco_format_save_path = '/home/jyoti/Desktop/csc8800/datasets/DoorDetectDataset/test.json'
# coco_format_save_path = '/home/jyoti/Desktop/csc8800/datasets/DoorDetectDataset/train.json'
# with open(coco_format_save_path,'w') as fw:
#     json.dump(write_json_context,fw) 
    
##############################################################################
import glob
import cv2
import json
import os
import numpy as np
path = 'F:/project_2/New_folder/data/downloads/' #path to label file yolo
label_file = glob.glob(path+'*txt')
file_number = 0
class_id =0
num_bboxes = 0
write_json_context = dict()
write_json_context['info'] = {'description': '', 'url': '', 'version': '', 'year': 2022 , 'contributor': '', 'date_created': '2022-04-17 11:00:08.5'}
write_json_context['licenses'] = [{'id': 1, 'name': None, 'url': None}]
write_json_context['images'] = []
write_json_context['annotations'] = []
texts=[]
categories =[]
for img_id,fi in enumerate(label_file):

    with open(fi,'r',encoding = 'utf-8') as f:  
        for j,l in enumerate(f):
            if '*' in l:
                text,x1,y1,_,_,x2,y2,_,_ = l[:-1].split('*')
            else:
                text,x1,y1,_,_,x2,y2,_,_ = l[:-1].split(',')
            if text not in texts:
                categories.append({'id':class_id,'name':text,'supercategory': "text"})
                class_id+=1
                texts.append(text)
            category_i= [i for i,j in enumerate(texts) if text == j][0]
            
            num_bboxes+=1
            bbox_dict = {}
            bbox_dict['id'] = num_bboxes
            bbox_dict['image_id'] = file_number
            bbox_dict['category_id'] = category_i
            bbox_dict['iscrowd'] = 0 # There is an explanation before
            h,w = int(x2)-int(x1), int(y2)-int(y1)
            bbox_dict['area']  = h * w
            x_coco = int(x1)
            y_coco = int(y1)
            if x_coco <0: #check if x_coco extends out of the image boundaries
                x_coco = 1
            if y_coco <0: #check if y_coco extends out of the image boundaries
                y_coco = 1
            bbox_dict['bbox'] = [x_coco,y_coco,w,h]
            bbox_dict['segmentation'] = [[x_coco,y_coco,x_coco+w,y_coco, x_coco+w, y_coco+h, x_coco, y_coco+h]]
            write_json_context['annotations'].append(bbox_dict)
            
        if os.path.exists(fi.split('.')[0] + '.jpg'):
            img_name = fi.split('.')[0] + '.jpg'
        elif os.path.exists(fi.split('.')[0] + '.png'):
            img_name = fi.split('.')[0] + '.png'
        try:
            img_path = img_name
        except:
            pass

        img_context = {}
        height,width = cv2.imread(img_path).shape[:2]
        img_context['file_name'] = img_name
        img_context['height'] = height
        img_context['width'] = width
        img_context['date_captured'] = '2021-02-12 11:00:08.5'
        img_context['id'] = file_number # image id
        img_context['license'] = 1
        img_context['coco_url'] =''
        img_context['flickr_url'] = ''
        write_json_context['images'].append(img_context)
        
        
        file_number+=1
write_json_context['categories'] = categories
coco_format_save_path = 'F:/project_2/New_folder/data/downloads/train.json'
with open(coco_format_save_path,'w',encoding='utf-8') as fw:
    json.dump(write_json_context,fw,indent=' ',ensure_ascii=False) 
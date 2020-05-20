
# coding: utf-8

# In[1]:


from video_preprocessing_functions import *


# In[2]:


#Label files are called : c0_action_labels.xml
#The correspoding videos are called : c0.mp4
filePath = ['c0_action_labels.xml', 'c1_action_labels.xml']
videoPath = ['c0.mp4', 'c1.mp4']
root = 'ucf24/'
labels_root = root + 'labels/'
images_root = root + 'rgb-images/'

target_size_x = 224
target_size_y = 224
x_size = 1280
y_size = 720
#Because we're using linear interpolation
x_scale = target_size_x/float(x_size)
y_scale = target_size_y/float(y_size)


# In[3]:


all_labels = get_labels(filePath)
#mkdir_label(all_labels, root, labels_root, images_root)
total_videos, all_clips = get_clips(filePath)
label_ids = generate_ids(all_clips)


# In[4]:


print('Total number of labels = ', len(all_labels))
print('Total number of labels with clips = ', len(all_clips))


# In[5]:


print('Creating Labels')
frames_for_video, label_file_counter = create_labels(filePath, labels_root, label_ids, all_labels,  x_scale, y_scale)
print('Creating Frames')
video_to_frame(filePath, videoPath, images_root, frames_for_video, all_labels, target_size_x, target_size_y)

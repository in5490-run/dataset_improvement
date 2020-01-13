

from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os, shutil

path = 'C:\\Users\\hakon\\OneDrive - Universitetet i Oslo\\IN5490\\dataset_imp\\test_set\\eval\\'
dest_dir = os.path.join(os.curdir, 'verified_set')
#path = Path("./test_set/eval/")
current_file = ''
file_suffix = '_comb.png'
files_to_remove = []
files_to_keep = []

def on_press(event):
    key = event.key
    if event.key == 'right':
        files_to_keep.append(current_file)               

    if event.key == 'left':
        files_to_remove.append(current_file)        
    plt.close('all')

def move_files():
    for i in files_to_keep:
        src_dir = os.path.join(os.curdir, 'test_set', 'data')
        x_file = os.path.join(src_dir, 'x', (i + '_x.png'))
        y_file = os.path.join(src_dir, 'y', (i + '_y.png'))

        shutil.copy(x_file, os.path.join(dest_dir, 'x'))
        shutil.copy(y_file, os.path.join(dest_dir, 'y'))

        

for i in range(20):
    plt.figure(figsize=(700,700))
    current_file = str(i)
    img = mpimg.imread(path + str(i) + file_suffix)
    img_plot = plt.imshow(img)
    plt.connect('key_press_event', on_press)
    plt.show()

print(*files_to_keep)
print(*files_to_remove, flush=True)

move_files()
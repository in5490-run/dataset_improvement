from PIL import Image
import numpy as np
from pathlib import Path
import os, webbrowser

img_path = Path("./test_set/data/")
save_path = Path("./test_set/eval/")

for i in range(20):
    print("Processing pic " + str(i))
    x_img = Image.open(img_path / 'x' / (str(i) + '_x.png'))
    y_img = Image.open(img_path / 'y' / (str(i) + '_y.png'))
    
    y_np = np.array(y_img.convert('RGBA'))


    y_np[:,:, 3] = (255 * (y_np[:, :, :3] != 255).any(axis=2)).astype(np.uint8)/4
    
    #y_np = np.where(y_np == [255, 255, 255], [0,0,0,255], y_np)

    y_img = Image.fromarray(y_np, mode='RGBA')
    x_img.convert('RGBA')
    #y_img = Image.blend(x_img, y_img, 0.25)



    comb_img = Image.alpha_composite(x_img, y_img)    
    path = (save_path / (str(i) + "_comb.png"))
    comb_img.save(path, format='PNG')

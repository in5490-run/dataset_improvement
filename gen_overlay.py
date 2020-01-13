from PIL import Image
import numpy as np

path = "/mnt/c/Users/hakon/OneDrive - Universitetet i Oslo/IN5490/dataset_imp/test_set/data/"

for i in range(500):
    print("Processing pic " + str(i))
    x_img = Image.open(path + "x/" + str(i) + "_x.png")
    y_img = Image.open(path + "y/" + str(i) + "_y.png")

    y_np = np.array(y_img.convert('RGBA'))
    y_np[:,:, 3] = (255 * (y_np[:, :, :3] != 255).any(axis=2)).astype(np.uint8)
    #y_np = np.where(y_np == [255, 255, 255], [0,0,0,255], y_np)

    y_img = Image.fromarray(y_np, mode='RGBA')
    y_img = Image.blend(x_img, y_img, 0.25)
    y_img.show()
    
    y_img.save(path + "y_new/" + str(i) + "_y_tr.png")

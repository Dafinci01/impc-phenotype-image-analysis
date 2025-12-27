import imagej 
import os 


#Start Imagej headless 
ij = image.init('sc.fiji:fiji', headless=True)


#folder contaning images to process 
image_folder ="../data/raw_images/"
results_folder = "../results/tables/"
os.mkdirs(results_folder, exist_ok=True)


#Example: run macro on all images in folder 

for img_file in os.listdir(image_folder):
    if img_file.endswith((".tif", ".png", ".jpg")):
        img_path = os.path.join(image_folder, img_file)
        ij.io().open(img_path)
        ij.py.run_macro(macro)
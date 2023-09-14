import os


#rename all images in res folder to format img and number

path = 'res'
files = os.listdir(path)
for i,file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, 'img' + str(i+1) + '.png'))
        
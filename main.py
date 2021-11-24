import cv2
import os

mainfolder = 'images'
myFolder = os.listdir(mainfolder)
print(myFolder)

for file in myFolder:
    path = mainfolder + '/' + file
    print(path)
    images = []
    mylist = os.listdir(path)
    print(mylist)
    for imgN in mylist:
        curimg = cv2.imread(f'{path}/{imgN}')
        curimg = cv2.resize(curimg, (0, 0),None, 0.5, 0.5)
        images.append(curimg)

    sticher = cv2.Stitcher.create()
    ret, pano = sticher.stitch(images)

    if ret == cv2.STITCHER_OK:
        print('success panaroma created')
        cv2.imwrite('panaroma.jpg', pano)
        cv2.imshow('Panorama', pano)
        cv2.waitKey()
        cv2.destroyAllWindows() 
    else:
        print("Error during Stitching")

print(len(images))



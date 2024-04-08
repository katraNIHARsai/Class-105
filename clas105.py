import os
import cv2

path = "Images"

images = []

for i in os.listdir(path):
    name,extension = os.path.splitext(i)
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path + '/' + i
        #print(file_name)
        images.append(file_name)
        
#print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
#print(size)

#cv2.VideoWriter_fourcc(*'DIVX'): This specifies the codec to be used for encoding the video. A codec is a method for encoding and decoding video data. 
# 'DIVX' is the FourCC code (Four Character Code) for the DivX codec. The cv2.VideoWriter_fourcc() function converts this string into the required codec format.
# Different codecs have different properties like compression efficiency, compatibility, etc.

out = cv2.VideoWriter('Projectsunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),15,size) #5 is frames per second

#for j in range(count - 1,0,-1):                                    #this is for sunrise
for j in range(0,count-1):                                          #this is for sunset      
    frame = cv2.imread(images[j])
    out.write(frame)
    
out.release()
print("Done!")
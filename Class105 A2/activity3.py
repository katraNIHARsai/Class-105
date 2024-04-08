import cv2
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("Unable to open the camera")

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)

fps = int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

out = cv2.VideoWriter('Boxing.mp4',cv2.VideoWriter_fourcc(*'DIVX'),10,(width,height))

while(True):
    ret,frame = vid.read()
    cv2.imshow("webcam",frame)
    out.write(frame)
    if cv2.waitKey(1) == 32:
        break

vid.release()
out.release()
cv2.destroyAllWindows()
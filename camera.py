import cv2

vid = cv2.VideoCapture(0)

while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    smolla = cv2.resize(frame, (200, (200 * frame.shape[0]) // frame.shape[1]))
    img_gray = cv2.cvtColor(smolla, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
    edges1 = cv2.Canny(image=img_blur, threshold1=25, threshold2=30) # Canny Edge Detection

    # Display the resulting frame
    cv2.imshow('frame', edges1)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
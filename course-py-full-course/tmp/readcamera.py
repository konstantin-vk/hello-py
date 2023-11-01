# this is the OpenCV 
import cv2 


#camera_backends = cv2.videoio_registry.getCameraBackends()
#print(camera_backends)
#print([
#    cv2.videoio_registry.getBackendName(apipref)
#    for apipref in camera_backends
#])

# input 
capture = cv2.VideoCapture(0)

while(True): 
    # Capture the video frame  by frame 
    okay, frame = capture.read()     # CAP_V4L /dev/video0
    if not okay:
        break
    
    # Display the resulting frame 
    cv2.imshow('frame', frame)       
    # the 'q' button is set as the quitting button you may use any desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# desctructors 
capture.release()
cv2.destroyAllWindows()
# Mon script OpenCV : Video_processing
#
import numpy as np
import cv2

#
def frame_processing(imgc):
     return imgc


if __name__ == '__main__':

    #
    cap = cv2.VideoCapture('Images2020/jurassicworld.mp4')

    #
    while (True):

        #
        ret, frame = cap.read()

        #
        if ret == True:
            #
            img = frame.copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #
            gray = frame_processing(gray)

            #
            cv2.imshow('MavideoAvant', frame)
            cv2.imshow('MavideoApres', gray)

        else:
            print('video ended')
            break

        if cv2.waitKey(1000) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
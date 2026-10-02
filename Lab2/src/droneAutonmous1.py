# take off, wait a sec, rotate 90 degrees, wait, rotate, wait, land

import threading
import cv2
from djitellopy import Tello
import keyboard
import time

condition = threading.Condition()
save_pic = False
tello = Tello()
tello.connect()
tello.streamon()

running = True
last_key = ''
def key_press():
    global save_pic
    global running
    global last_key
    landed = True
    rotation_degree = 90
    movement_distance = 20 ## in cm
    
    while running:
        # print("KEY_ PRESSES**********")
        if keyboard.is_pressed('k'):
            print('============ Initiating Autonomous Action 1 (T0=W=R90=W=R(-90)=L) ============')
            time.sleep(1)
            landed = False
            print('1. Initiating Take off.......')
            tello.takeoff()
            print('====== Take off done =====')

            print('2. Wait 1 second........')
            time.sleep(1)

            print('3. Rotate 90 degree clckwise........')
            tello.rotate_clockwise(rotation_degree)
            print('====== Rotation complete =====')

            print('4. Wait 1 second.......')
            time.sleep(1)

            print('3. Rotate 90 degree Anti-clckwise........')
            tello.rotate_counter_clockwise(rotation_degree)
            print('====== Rotation complete =====')

            print('5. Wait 1 second........')
            time.sleep(1)

            print('6. Initiating Landing.........')
            if landed == False:
                tello.land()
                print ('===== Landing done =====')
                print("break the loop")
                running = False
            


def skip_holdDown_key(key):
    while keyboard.is_pressed(key):
        pass

def stream_camera():
    global save_pic
    global last_key
    global running

    counter = 0
    counter_show = 0
    # running = True
    while running:
        counter_show += 1
        frame_read = tello.get_frame_read()

        if frame_read is not None:
            # print("show pic", counter_show)
            frame = frame_read.frame
            cv2.imshow("picture.png", frame)

        if cv2.waitKey(1) & save_pic:
            last_key = ''
            save_pic = False
            counter += 1
            picture_name = './pics/set7pic' + str(counter) + '.jpg'
            print("PICTURE SAVED",picture_name)
            cv2.imwrite(picture_name, frame)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            running = False
            
        


stream_thread = threading.Thread(target=stream_camera)
key_press_thread = threading.Thread(target=key_press)

stream_thread.start()
key_press_thread.start()

key_press_thread.join()
stream_thread.join()

cv2.destroyAllWindows() 
exit()
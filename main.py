import os
import datetime
import cv2
import time
from skimage.measure import compare_ssim
def adb_0_capture():
    now = datetime.datetime.now()
    timestamp = now.strftime('%d_%H_%M_%S')
    os.system('adb exec-out screencap -p -d 0 > screen_d(0){}.png'.format(timestamp))

    time.sleep(1)
    filepath = os.path.abspath('./screen_d(0){}.png'.format(timestamp))

    return filepath

def adb_1_capture():
    now = datetime.datetime.now()
    timestamp = now.strftime('%d_%H_%M_%S')
    os.system('adb exec-out screencap -p -d 1 > screen_d(1){}.png'.format(timestamp))

    time.sleep(1)
    filepath = os.path.abspath('./screen_d(1){}.png'.format(timestamp))

    return filepath

def adb_0_image_compare(data):
    ref = cv2.imread(data)
    com = cv2.imread(adb_0_capture())

    result = ref.copy()

    temp_diff = cv2.subtract(ref, com)

    gray_ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    gray_com = cv2.cvtColor(com, cv2.COLOR_BGR2GRAY)

    (score, diff) = compare_ssim(gray_ref, gray_com, full=True)
    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    temp_diff[thresh == 255] = [0, 0, 255]
    result[thresh == 255] = [0, 0, 255]
    now = datetime.datetime.now()

    timstamp = now.strftime("%d_%H_%M_%S")
    cv2.imwrite("./result{}.png".format(timstamp), result)

    print ("Similarity: {}".format(score*100))

    return score*100

def adb_1_image_compare(data):
    ref = data
    com = adb_1_capture()

    return

if __name__ == '__main__':

    adb_0_image_compare("D:\excelrunner_report\captured_image\\reference.bmp")
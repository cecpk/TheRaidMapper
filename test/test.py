import cv2
import numpy as np
from pytesseract import image_to_string
from PIL import Image
import datetime
import time


def test1():
    rt = Image.open("test_X.png")
    gray = rt.convert('L')
    bw = gray.point(lambda x: 0 if x<150 else 255, '1')
    bw.save("234.png")
    text1 = image_to_string(bw,config='--psm 10 --oem 3 -c tessedit_char_whitelist=xXoO0')
    print text1

    
def getHatchTime(data):
        zero = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        unix_zero = (zero-datetime.datetime(1970,1,1)).total_seconds()
        hour_min_divider = data.find(':')
        if hour_min_divider != -1:
            AM = data.find('AM')
            PM = data.find('PM')
            if AM >= 4:
                data = data.replace('A','').replace('M','').replace('~','').replace('-','').replace(' ','')
                hour_min = data.split(':')
                ret, hour_min = checkHourMin(hour_min)
                if ret == True:
                    return int(unix_zero)+int(hour_min[0])*3600+int(hour_min[1])*60
                else:
                    return -1
            elif PM >= 4:
                data = data.replace('P','').replace('M','').replace('~','').replace('-','').replace(' ','')
                hour_min = data.split(':')
                ret, hour_min = checkHourMin(hour_min)
                if ret == True:
                    if hour_min[0] == '12':
                        return int(unix_zero)+int(hour_min[0])*3600+int(hour_min[1])*60
                    else:
                        return int(unix_zero)+(int(hour_min[0])+12)*3600+int(hour_min[1])*60
                else:
                    return -1
            else:
                data = data.replace('~','').replace('-','').replace(' ','')
                hour_min = data.split(':')
                ret, hour_min = checkHourMin(hour_min)
                if ret == True:
                    return int(unix_zero)+int(hour_min[0])*3600+int(hour_min[1])*60
                else:
                    return -1
        else:
            return -1

def checkHourMin(hour_min):
        hour_min[0] = unicode(hour_min[0].replace('O','0').replace('o','0').replace('A','4'))
        hour_min[1] = unicode(hour_min[1].replace('O','0').replace('o','0').replace('A','4'))
        if (hour_min[0]).isnumeric()==True and (hour_min[1]).isnumeric()==True:
            return True, hour_min
        else:
            return False, hour_min
            
if __name__ == '__main__':
    test1()
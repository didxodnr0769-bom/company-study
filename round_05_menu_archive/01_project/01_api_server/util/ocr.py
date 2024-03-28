import cv2
import pytesseract
import numpy as np
import urllib.request

LANG = 'kor_best'

# 이미지에서 텍스트 추출 요청 
# url {str} : 이미지 url
def request_extract(url,file_name):
    # 웹에서 이미지를 읽어와 NumPy 배열로 변환
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # 이미지 보정
    corrected_img = correction_image(image)
    # 전처리된 이미지를 파일로 저장합니다.
    cv2.imwrite(file_name, corrected_img)

    # 텍스트 추출
    return extract_text(corrected_img)


# opencv를 이용한 텍스트 추출전 이미지 보정 
def correction_image(image):
    black_color_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(black_color_img,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return threshold_img
    

# 이미지에서 텍스트 추출
def extract_text(image):

    custom_config = '-l kor --oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config, lang=LANG)

    return text



    
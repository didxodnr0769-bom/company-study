import cv2
import pytesseract
import numpy as np
import urllib.request

# 로컬 파일이 아닌 웹에 있는 이미지를 읽어와 텍스트를 추출하는 로직 테스트

#color -> grayscale
def gray_scale(image):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return result

#grayscale -> binary
def image_threshold(image):
    result = cv2.threshold(image,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return result


image_path = "https://k.kakaocdn.net/dn/jzyyk/btsFNuHErvc/wh7Ac2geiGoRzarttQvfe0/img_l.jpg"
LANG = 'kor_best'



# 웹에서 이미지를 읽어와 NumPy 배열로 변환
resp = urllib.request.urlopen(image_path)
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)


image_can_gray = gray_scale(image)
image_can_binary = image_threshold(image_can_gray)


# 전처리된 이미지를 파일로 저장합니다.
cv2.imwrite('test.jpeg', image_can_binary)

custom_config = '--oem 3 --psm 4'
text = pytesseract.image_to_string(image_can_binary, config=custom_config, lang=LANG)


print(text)


import cv2
import pytesseract
import numpy as np

image_path = 'food1.jpeg'
LANG = 'kor_best'

# 이미지 파일 로드
image_can = cv2.imread(image_path)


#color -> grayscale
def gray_scale(image):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return result

#grayscale -> binary
def image_threshold(image):
    result = cv2.threshold(image,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return result



image_can_gray = gray_scale(image_can)
image_can_binary = image_threshold(image_can_gray)

# dst = image_can_binary[0:1200, 0:800].copy()

image_result = image_can_binary


# 전처리된 이미지를 파일로 저장합니다.
cv2.imwrite('test.jpeg', image_result)

# 이미지에서 텍스트 추출
# custom_config = r'--psm 4'

custom_config = '-l kor --oem 3 --psm 6'
text = pytesseract.image_to_string(image_result, config=custom_config, lang=LANG)
# 추출한 텍스트 출력
print(text)




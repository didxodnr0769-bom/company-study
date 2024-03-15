import cv2
import pytesseract
from PIL import Image

image_path = 'food2.jpeg'
LANG = 'kor_best'

# 이미지 파일 로드
image = cv2.imread(image_path)



# 이미지 전처리를 위해 흑백으로 변환
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thr = cv2.threshold(gray,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(thr, lang=LANG)

# 추출한 텍스트 출력
print(text)

print("----------------비교----------------")
# 이미지 파일 경로 설정

# 이미지 로드
img = Image.open(image_path)
# 이미지에서 텍스트 추출
text2 = pytesseract.image_to_string(img, lang=LANG) 

print(text2)
from PIL import Image
import pytesseract

# Tesseract 경로 설정 (Windows 사용자만 필요, macOS/Linux는 일반적으로 필요 없음)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일 경로 설정
image_path = 'food1.jpeg'

# 이미지 로드
img = Image.open(image_path)

# 이미지에서 텍스트 추출
text = pytesseract.image_to_string(img, lang='kor_best') # 언어가 영어가 아닌 경우 'eng'를 해당 언어 코드로 변경

print(text)
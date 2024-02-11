import cv2
import pytesseract
# Tesseract path
t_path = r"C:\Users\mn Technology Group\Documents\Web pages\Arduino\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = t_path
image = cv2.imread("./test.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# Find the single largest contour = a single ROI
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
largest_cnt = max(cnts, key=cv2.contourArea)
# Extract the ROI based on the largest contour
x, y, w, h = cv2.boundingRect(largest_cnt)
roi = image[y:y+h, x:x+w]
# Perform OCR on the ROI
text = pytesseract.image_to_string(roi, config='--psm 10')
# Display text
print(text)
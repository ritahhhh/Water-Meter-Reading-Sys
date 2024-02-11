import cv2
import pytesseract

# Path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mn Technology Group\Documents\Web pages\Arduino\tesseract.exe'  # Update this with your Tesseract path

def extract_reading(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Check if the image is successfully loaded
    if img is None:
        print(f"Error: Unable to load image at '{image_path}'")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to enhance text visibility
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Use pytesseract to perform OCR on the thresholded image
    text = pytesseract.image_to_string(thresholded)

    # Clean up the extracted text (remove non-numeric characters)
    reading = ''.join(filter(str.isdigit, text))

    return reading

if __name__ == "__main__":
    # Replace 'your_image_path.jpg' with the actual path to your image
    image_path = r'C:\Users\mn Technology Group\Documents\Web pages\Arduino\test.jpg'
    
    extracted_reading = extract_reading(image_path)

    if extracted_reading is not None:
        print("Extracted Reading:", extracted_reading)

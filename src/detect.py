import cv2
import pytesseract
from ultralytics import YOLO

# Load your trained YOLO model
model = YOLO('models/best_numberplatedetection.pt')

def run(image):
    """
    Predicts and plots the bounding boxes on the given image using the trained YOLO model.
    Also performs OCR on the detected bounding boxes to extract text.
    
    Parameters:
    image (ndarray): Image array in BGR format (OpenCV).
    
    Returns:
    tuple: A tuple containing the processed image and a list of detected texts.
    """
    # Perform prediction on the image using the model
    results = model.predict(image, device='cpu')

    detected_texts = []  # Initialize a list to store detected texts

    # Extract the bounding boxes and labels from the results
    for result in results:
        for box in result.boxes:
            # Get the coordinates of the bounding box
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            # Get the confidence score of the prediction
            confidence = box.conf[0]

            # Draw the bounding box on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw the confidence score near the bounding box
            cv2.putText(image, f'{confidence*100:.2f}%', (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

            # Crop the bounding box from the image for OCR
            roi = image[y1:y2, x1:x2]

            # Perform OCR on the cropped image
            text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
            detected_texts.append(text)  # Append detected text to the list

    # Convert the image to RGB format for displaying in Streamlit
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return image_rgb, detected_texts  # Return both the image and detected texts

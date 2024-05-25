import os
import cv2
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel


def perform_ocr_on_folder():
    # Initialize the TrOCR model and processor
    processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-handwritten')
    model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-large-handwritten')
    concatenated_text = ""
    def perform_ocr(image):
        # Preprocess the image using the TrOCR processor
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
    
        # Generate text using the TrOCR model
        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    
        return generated_text

    # Get the list of files in the folder
    roi_folder_path = "temporary/new/"
    files_in_folder = os.listdir(roi_folder_path)

    # Count the number of image files (assuming they have the .png extension)
    num_images = sum(1 for file in files_in_folder if file.endswith(".jpeg"))

    # Initialize the concatenated text
    output_file_path = "temporary/concatenated.txt"
    

    # Iterate through the files in the folder
# Iterate through the files in the folder
    for i in range(0, num_images):
        # Construct the file name
        filename = f"detection_{i}.jpeg"
    
        # Construct the full path to the ROI image
        roi_image_path = os.path.join(roi_folder_path, filename)
    
        # Load the ROI image
        roi = cv2.imread(roi_image_path)

        # Convert OpenCV ROI to PIL Image
        roi_pil = Image.fromarray(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
    
        # Perform OCR on the current ROI
        detected_text = perform_ocr(roi_pil)
    
        # Concatenate the detected text
        concatenated_text += detected_text + " "

    # Open the output file in write mode and save the text
    with open(output_file_path, "w", encoding='utf-8') as file:
        file.write(concatenated_text)

    # print("OCR performed and output saved successfully!")

    return concatenated_text

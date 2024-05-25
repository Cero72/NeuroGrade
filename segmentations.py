import os
import json
from PIL import Image

def run_model():
    results_dir = "temporary/results"
    image_path = "temporary/uploaded/2.jpeg"
    # Run object detection using surya_detect command
    command = f"surya_detect {image_path} --images --results_dir {results_dir}"
    try:
        os.system(command)
    except Exception as e:
        print(f"Error occurred during object detection: {e}")

def save_bbox_images():
    """
    Function to perform object detection and save individual bounding box regions as images.
    """
    # Define the results directory
    save_dir = "temporary/new/"

    # Clear all files from the directory before saving new content
    for file_name in os.listdir(save_dir):
        file_path = os.path.join(save_dir, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error while deleting file {file_path}: {e}")

    # Define the path to the JSON file containing detection results
    json_file_path = "temporary/results/2/results.json"

    # Load the results from JSON
    with open(json_file_path, 'r') as f:
        results = json.load(f)

    # Load the image
    image_path = "temporary/uploaded/2.jpeg"
    image = Image.open(image_path)

    # Convert the image to RGB mode if it's in palette mode
    if image.mode == 'P':
        image = image.convert('RGB')

    # Iterate over each detection
    for _, detections in results.items():
        for detection in detections:
            # Iterate over each bounding box in the detection
            for idx, bbox_info in enumerate(detection['bboxes']):
                # Extract bounding box coordinates
                bbox = bbox_info['bbox']
                x_min, y_min, x_max, y_max = bbox

                # Crop the bounding box region from the image
                bbox_region = image.crop((x_min, y_min, x_max, y_max))

                # Save the cropped region as a separate image
                save_path = os.path.join(save_dir, f"detection_{idx}.jpeg")
                bbox_region.save(save_path)

    print("Bounding box images saved successfully!")

# Example usage
run_model()
save_bbox_images()

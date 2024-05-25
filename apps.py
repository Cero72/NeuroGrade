import streamlit as st
from PIL import Image
import os
from dectections import perform_ocr_on_folder
from segmentations import run_model, save_bbox_images
from grading import llm, read_text_from_file

# Function to perform segmentation and text extraction
def extract_segmentation_and_text():
    # Run segmentation model
    run_model()
    save_bbox_images()
    # Load segmented image
    segmented_image_path = "temporary/results/2/2_0_bbox.png"
    segmented_image = Image.open(segmented_image_path)
    # Perform OCR on segmented image to extract text
    text = perform_ocr_on_folder()
    return segmented_image, text

# Function to save text to a file
def save_text_to_file(text, file_path):
    with open(file_path, "w") as f:
        f.write(text)

# Main function to display and save uploaded image
def display_and_save_uploaded_image():
    # Initialize session state
    if 'question' not in st.session_state:
        st.session_state.question = ""
    if 'reference_answer' not in st.session_state:
        st.session_state.reference_answer = ""
    if 'segmentation_text_clicked' not in st.session_state:
        st.session_state.segmentation_text_clicked = False
    if 'segmented_image' not in st.session_state:
        st.session_state.segmented_image = None
    if 'extracted_text' not in st.session_state:
        st.session_state.extracted_text = ""

    # Prompt user to enter the question
    st.session_state.question = st.text_area("Enter the question", value=st.session_state.question)
    if st.button("Save Question"):
        # Save question to file
        question_file_path = "temporary/question.txt"
        save_text_to_file(st.session_state.question, question_file_path)
        st.success("Question saved successfully!")

    # Prompt user to enter the reference answer
    st.session_state.reference_answer = st.text_area("Enter the reference answer", value=st.session_state.reference_answer)
    if st.button("Save Reference Answer"):
        # Save reference answer to file
        reference_answer_file_path = "temporary/reference.txt"
        save_text_to_file(st.session_state.reference_answer, reference_answer_file_path)
        st.success("Reference answer saved successfully!")

    # Prompt user to upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = Image.open(uploaded_file)

        # Convert the image to JPEG format
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Hardcoded save path and filename
        save_dir = r"D:\final_projects\final year project\temporary\uploaded"
        save_filename = "2.jpeg"

        # Save the uploaded image to the hardcoded directory with the fixed filename "2.jpeg"
        save_path = os.path.join(save_dir, save_filename)
        image.save(save_path)

        # Add a button to execute segmentation and text extraction
        if st.button("Extract Segmentation and Text"):
            # Execute segmentation function and display results
            segmented_image, text = extract_segmentation_and_text()
            st.session_state.segmented_image = segmented_image
            st.session_state.extracted_text = text
            st.session_state.segmentation_text_clicked = True

    if st.session_state.segmentation_text_clicked:
        # Display the segmented image
        st.image(st.session_state.segmented_image, caption="Segmented Image", use_column_width=True)

        # Display the extracted text
        st.write(f"Extracted Text: {st.session_state.extracted_text}")

        # Add a button to grade the answer
        if st.button("Grade"):
            # Get question, reference answer, and candidate answer from files
            question = read_text_from_file("temporary/question.txt")
            reference_answer = read_text_from_file("temporary/reference.txt")
            candidate_answer = st.session_state.extracted_text

            # Run the llm function
            grade = llm(question, reference_answer, candidate_answer)

            # Display the grade
            st.write(f"Grade: {grade}")

# Example usage
display_and_save_uploaded_image()

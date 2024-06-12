**Automated Grading System for Handwritten Answers**

This repository contains the implementation of an automated system for grading handwritten subjective answers, leveraging advanced computer vision, natural language processing, and large language model techniques.

## Overview

The proposed system aims to automate the traditionally labor-intensive task of grading handwritten responses, offering a scalable and efficient solution with the potential to transform education assessment practices. The system utilizes the following key components:

1. **Text Detection**: The [Surya](https://github.com/VikParuchuri/surya/tree/master) for text line detection in documents.

2. **Handwritten Text Recognition**: The TrOCR (Transformer-based Optical Character Recognition) model is used for recognizing and transcribing handwritten text within the detected regions.

3. **Answer Evaluation**: An LLM (API) is employed to evaluate the transcribed handwritten answers against a reference answer key, providing a consistent grading mechanism.

## Features

- Accurate text detection in handwritten images using CRAFT (SuryaOCR)
- Robust handwritten text recognition with TrOCR
- Automated grading of subjective answers using a Gemini API
- Consistent and scalable evaluation of handwritten responses
- Potential to transform education assessment practices

# In order to use this tool, you need to follow steps mentioned below : 
1. Generate and add your Gemini API key in the grading.py file
2. run the command "streamlit run apps.py" in the terminal
3. Follow the link 

# How to use this tool ?
1. Enter the question to answer needed to graded, save the question
2. Enter the actual answer to the question, save it
3. Drag or upload the handwritten answer image and click the extract and segment button
4. Once the answer is converted to digital text, click the grade button and get the grade

# Some necessary things to have :
CUDA installed and configured if using the GPU
libraries like streamlit, NumPy, Cv2, PyTorch, PIL need to be installed
The [Surya](https://github.com/VikParuchuri/surya/tree/master) OCR and [TrOCR](https://github.com/microsoft/unilm/tree/master/trocr) are necessary 

# Thanks

This work would not have been possible without amazing open source AI work:

- [Segformer](https://arxiv.org/pdf/2105.15203.pdf) from NVIDIA
- [TrOCR](https://github.com/microsoft/unilm/tree/master/trocr) for handwritten text recognition
- [Surya](https://github.com/VikParuchuri/surya/tree/master) for text line detection
- [Donut](https://github.com/clovaai/donut) from Naver
- [transformers](https://github.com/huggingface/transformers) from huggingface
- [CRAFT](https://github.com/clovaai/CRAFT-pytorch), a great scene text detection model

Thank you to everyone who makes open source AI possible.

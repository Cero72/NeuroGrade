import google.generativeai as genai
genai.configure(api_key="")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def get_user_input():
  """Gets the user input."""

  # Get the question
  question_file_path = "temporary/question.txt"
  with open(question_file_path, "r") as f:
    question = f.read()

  # Get the reference answer
  reference_answer_file_path = "temporary/reference.txt"
  with open(reference_answer_file_path, "r") as f:
    reference_answer = f.read()

  candidate_answer_file_path = "temporary/concatenated.txt"
  with open(candidate_answer_file_path, "r") as f:
    candidate_answer = f.read()

  # Return the user input
  return question, reference_answer, candidate_answer


def read_text_from_file(file_path):
  with open(file_path, "r") as f:
    reference_answer = f.read()
  return reference_answer

def format_text(question, reference_answer, candidate_answer):
  """Converts the user input into the desired format."""

  # Return the formatted text
  return f"""you are a subjective answer evaluator that grade's the candidates answer as compared to the correct answer that is the reference answer in the range of 1-5 in this format GRADE : "give grade." then FEEDBACK on a new line : "give the explanation for your grading in few lines" now evaluate these and ignore spelling mistakes :

question : "{question}"

reference answer: {reference_answer}

candidate answer:
{candidate_answer}
"""

def llm(question, reference_answer, candidate_answer):
  """Runs the model."""
  # question, reference_answer, candidate_answer = get_user_input()
  user_input = format_text(question, reference_answer, candidate_answer)

  # Start a conversation with the model
  convo = model.start_chat()

  # Send the user input to the model
  convo.send_message(user_input)

  # Print the model's response
  # print(convo.last.text)
  return convo.last.text
  



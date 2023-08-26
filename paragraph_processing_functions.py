import openai

# Function to call OpenAI API for summarization
def extract_key_points(paragraph):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide an unordered Markdown list that someone could read to quickly understand what was talked about. The list should be in the same langage as the input text."
            },
            {
                "role": "assistant",
                "content": "Identify the language of the text you are provided. Generate your responses in the original language of the text."
            },
            {
                "role": "assistant",
                "content": "Format your response as an unordered Markdown list."
            },
            {
                "role": "user",
                "content": paragraph
            }
        ]
    )
    return response['choices'][0]['message']['content']

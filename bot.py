# Import necessary modules
import os

from groq import Groq

def get_response(prompt):
    # Define the file path
    file_path = 'chatbot_log.txt'

    # Check if the file exists, if not, create it
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("Prompt\tResponse\n")  # Write the header

    # Initialize the Groq client
    client = Groq(
        api_key="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",
    )

    # Get the chat completion
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    # Extract the response
    response = chat_completion.choices[0].message.content

    # Write the prompt and response to the file
    with open(file_path, 'a') as file:
        file.write(f"{prompt}\t{response}\n")

    return response

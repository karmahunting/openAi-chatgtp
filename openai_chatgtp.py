import openai

# Set up the OpenAI API key
openai.api_key = ""

# Use the GPT-3 engine
engine = "text-davinci-002"

# Set up the prompt
prompt = "Here is your awnser:"

while True:
    # Get user input
    user_input = input("Enter your message: ")

    # Check if the user wants to exit the chatbot
    if user_input.lower() == "exit":
        break

    # Generate a response to the user input using the GPT-3 engine
    response = openai.Completion.create(
        engine=engine,
        prompt=user_input,
        max_tokens=1024,
        n = 1,
        stop = None
    )

    # Print the prompt and the response
    print(f"{prompt}\n{response['choices'][0]['text']}")

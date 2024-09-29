import random
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Initialize the model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# List of fun facts
fun_facts = [
    "Did you know that octopuses have three hearts?",
    "A group of flamingos is called a 'flamboyance'.",
    "Bananas are berries, but strawberries aren't!",
    "Honey never spoils and can last thousands of years!",
]

user_name = None  # Variable to store the user's name

# Predefined responses to make the chatbot more engaging
predefined_responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you?": "I'm just a program, but I'm here to assist you!",
    "tell me a fact": "Sure! Did you know that honey never spoils?",
}

def chat_with_bot():
    global user_name  # Access the global variable
    print("Welcome to the Language Learning Chatbot! Type 'quit' to exit.")

    # Ask for the user's name
    while user_name is None:
        user_input = input("You: What's your name? ")
        if user_input.strip():  # Check if input is not empty
            user_name = user_input.strip()
            print(f"Bot: Nice to meet you, {user_name}! How can I assist you today?")
        else:
            print("Bot: Please enter a valid name.")

    chat_history_ids = None

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: It was great chatting with you! Have a wonderful day!")
            break

        # Normalize user input for predefined responses
        user_input_lower = user_input.lower()

        # Check for predefined responses
        if user_input_lower in predefined_responses:
            print(f"Bot: {predefined_responses[user_input_lower]}")
            continue

        # Random fun fact
        if "fact" in user_input_lower:
            print(f"Bot: {random.choice(fun_facts)}")
            continue
        
        # Encode the new user input and add the eos_token
        new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

        # Append the new user input to the chat history
        if chat_history_ids is None:
            chat_history_ids = new_user_input_ids
        else:
            chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)

        # Get the bot's response
        bot_response_ids = model.generate(chat_history_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

        # Get the bot's response text
        bot_response = tokenizer.decode(bot_response_ids[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)

        # Print the bot's response
        print(f"Bot: {bot_response}")

        # Update chat history
        chat_history_ids = bot_response_ids

if __name__ == "__main__":
    chat_with_bot()

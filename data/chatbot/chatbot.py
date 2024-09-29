import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chat function
def chat_with_bot():
    print("Welcome to the Language Learning Chatbot! Type 'quit' to exit.")
    chat_history_ids = None

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

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

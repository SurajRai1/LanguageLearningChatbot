import random

# Example personality traits
personality_traits = {
    "quirky": [
        "I'm just a bunch of code, but I like to think I'm fun!",
        "I might not have a favorite color, but if I did, it would be #00ff00!",
    ],
    "friendly": [
        "Hey there! I’m here to help you with anything you need!",
        "I love chatting with you, it brightens my day!",
    ],
}

# Choose a personality
chosen_personality = "friendly"  # Change to "quirky" for a different style

# To store user info
user_info = {}

# Function to generate a simple response
def generate_response(user_input):
    if "interesting fact" in user_input.lower():
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!"
    elif "like" in user_input.lower():
        interest = user_input.split("like")[-1].strip()
        return f"Oh, you like {interest}? That's cool!"
    elif "tell me about programming" in user_input.lower():
        return "Programming is the process of designing and building executable computer software to accomplish a specific task."
    elif "help" in user_input.lower():
        return "Of course! I can help with language learning, facts, and more. Just ask!"
    elif "your name" in user_input.lower():
        return "I'm a chatbot created to help you learn and have fun!"
    elif "weather" in user_input.lower():
        return "I can't check the weather, but I hope it's sunny where you are!"
    elif "joke" in user_input.lower():
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
    else:
        return "That's interesting! Tell me more."

# Function to chat with the bot
def chat_with_bot():
    global user_info
    print("Welcome to the Language Learning Chatbot! Type 'quit' to exit.")

    # Ask for the user's name
    user_name = input("What's your name? ")
    user_info['name'] = user_name
    print(f"Bot: Nice to meet you, {user_name}!")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Bot: It was great chatting with you! Have a wonderful day!")
            break

        # Engage with personality
        if chosen_personality == "friendly":
            response = random.choice(personality_traits["friendly"])
            print(f"Bot: {response}")
        else:
            response = random.choice(personality_traits["quirky"])
            print(f"Bot: {response}")

        # Generate a response
        bot_reply = generate_response(user_input)
        print(f"Bot: {bot_reply}")

if __name__ == "__main__":
    chat_with_bot()

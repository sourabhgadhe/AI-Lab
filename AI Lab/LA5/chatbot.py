import random

# Define some responses
greetings = ["Hello! Welcome to our pizza ordering service.", "Hi there! How can I help you today?", "Good day! How may I assist you?"]
sizes = ["small", "medium", "large"]
goodbyes = ["Thank you for ordering with us!", "Have a nice day!", "See you again!"]

# Define the chatbot function
def chatbot():
    print("ChatBot:",random.choice(greetings))
    while True:
        # Get user input
        user_input = input("You: ").lower() 
        
        # Check for exit command
        if user_input == "exit":
            print(random.choice(goodbyes))
            break
        
        #Check for pizza size
        # below expression generates a sequence of boolean values based on whether each key in sizes is present in the user's input. 
        # For example, if the user's input is "I want a small pizza", this generator expression will generate (True, False, False) because "small" is the first key in sizes.any() then checks if any of these values are True. If at least one key in sizes is present in the user's input, any() returns True. Otherwise, it returns False.

        if any(s for s in sizes if s in user_input):
            size = next((s for s in sizes if s in user_input))
            if size:
                print(f"ChatBot: Great, a {size} pizza !")
            else:
                print("ChatBot: I'm sorry, I didn't catch that. What size pizza would you like?")

        # Check for order confirmation
        elif "yes" in user_input:
            print("ChatBot: Thank you for your order !")
        
        # Handle all other input
        else: 
            print("ChatBot: I'm sorry, I didn't catch that. Can you please repeat your order?")
            
# Call the chatbot function
chatbot()

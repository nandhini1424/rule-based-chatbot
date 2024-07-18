class RuleBasedChatbot:
    def __init__(self):
        self.to_do_list = []

    def greet(self):
        return "Hello! How can I assist you today?"

    def respond(self, user_input):
        user_input = user_input.lower()
        if "hello" in user_input or "hi" in user_input:
            return self.greet()
        elif "how are you" in user_input:
            return "I'm just a bot, but I'm here to help you!"
        elif "what is your name" in user_input:
            return "I'm your helpful chatbot."
        elif "add to do" in user_input:
            return self.add_to_do(user_input)
        elif "show to do" in user_input or "list to do" in user_input:
            return self.show_to_do_list()
        elif "how to make" in user_input:
            return self.provide_recipe(user_input)
        elif "exit" in user_input or "bye" in user_input:
            return "Goodbye! Have a great day!"
        else:
            return "I'm sorry, I don't understand that. Can you please clarify?"

    def add_to_do(self, user_input):
        item = user_input.replace("add to do", "").strip()
        self.to_do_list.append(item)
        return f"Added '{item}' to your to-do list."

    def show_to_do_list(self):
        if not self.to_do_list:
            return "Your to-do list is empty."
        return "Your to-do list:\n" + "\n".join(self.to_do_list)

    def provide_recipe(self, user_input):
        dish = user_input.replace("how to make", "").strip()
        recipes = {
            "pasta": "To make pasta: 1. Boil water. 2. Cook pasta for 8-10 minutes. 3. Drain and serve.",
            "omelette": "To make an omelette: 1. Beat eggs. 2. Pour into a heated pan. 3. Cook until set. 4. Fold and serve.",
        }
        return recipes.get(dish.lower(), "Sorry, I don't have a recipe for that dish.")

def chat():
    chatbot = RuleBasedChatbot()
    print(chatbot.greet())
    
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("Bot: " + response)
        
        if "goodbye" in response.lower():
            break

chat()

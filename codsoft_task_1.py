import random

class FoodOrderChatbot:
    def __init__(self):
        self.responses = {
            "greetings": ["Hello!", "Hi there!", "Hey!"],
            "farewells": ["Goodbye!", "See you later!", "Take care!"],
            "jokes": ["Why don't scientists trust atoms? Because they make up everything!",
                      "I told my wife she was drawing her eyebrows too high. She looked surprised.",
                      "Parallel lines have so much in common. It’s a shame they’ll never meet."],
            "name": "I'm just a chatbot developed by MHZ.",
            "age": "I'm sorry, I'm not programmed to know my age.",
            "gratitude": ["You're welcome!", "Glad I could help!", "No problem!"],
            "customize": ["What will you like to order", "I'm here to help you"],
            "capabilities": "I can tell jokes, provide information about myself, and respond to greetings, farewells, and gratitude."
        }
        self.recommended_questions = {
            "default": ["Can you tell me a joke?", "What's your name?", "How can you help me?","What's on the menu?", "Do you have any specials?", "Can I customize my order?","How can I provide feedback on my order?", "Is there a customer satisfaction survey?", "Can I leave a review?","What payment methods do you accept?", "Is there a minimum order for delivery?", "Do you offer any discounts?","How long will my order take?", "Can you track my delivery?", "Is my food ready yet?"]
        }

    def respond(self, user_input):
        response = self.handle_intent(user_input)
        if not response:
            response = self.get_recommendation(user_input)
            response = "You can ask: " + response
        return response

    def handle_intent(self, user_input):
        if self.check_intent(user_input, ["hi", "hello", "hey"]):
            return random.choice(self.responses["greetings"])
        elif self.check_intent(user_input, ["payment", "pay"]):
            return self.payment_options()
        elif self.check_intent(user_input, ["bye", "goodbye"]):
            return random.choice(self.responses["farewells"])
        elif self.check_intent(user_input, ["customize"]):
            return random.choice(self.responses["customize"])
        elif self.check_intent(user_input, ["joke", "tell me a joke"]):
            return random.choice(self.responses["jokes"])
        elif self.check_intent(user_input, ["name", "who are you", "intro"]):
            return self.responses["name"]
        elif self.check_intent(user_input, ["your age", "how old are you"]):
            return self.responses["age"]
        elif self.check_intent(user_input, ["thank you", "thanks"]):
            return random.choice(self.responses["gratitude"])
        elif self.check_intent(user_input, ["status", "order status", "track"]):
            return self.check_order_status()
        elif self.check_intent(user_input, ["ready", "preparation", "prepared", "long"]):
            return self.order_preparation_time()
        elif self.check_intent(user_input, ["delivery","minimum order", "delivery charges","minimum"]):
            return self.charges_and_minimum()
        elif self.check_intent(user_input, ["order", "food", "hungry"]):
            return self.take_order()
        elif self.check_intent(user_input, ["discount"]):
            return self.discounts()
        elif self.check_intent(user_input, ["menu", "food options"]):
            return self.food_options()
        elif self.check_intent(user_input, ["special", "meal of day","today"]):
            return self.special_food()
        elif self.check_intent(user_input, ["feedback", "review","survey","satisfaction","leave"]):
            return self.leave_feedback()
        elif self.check_intent(user_input, ["help", "work"]):
            return self.work()

    def check_intent(self, user_input, keywords):
        return any(keyword in user_input.lower() for keyword in keywords)

    def take_order(self):
        return "Sure, what would you like to order?"

    def special_food(self):
        return "Sure, We have pepparoni pizza as special"

    def charges_and_minimum(self):
        return "There are no delivery charges and no minimum order requirements"
    def work(self):
        return "I can take your order, tell you a joke, check your order status?"

    def check_order_status(self):
        return "I'm sorry, I cannot provide the status of your order/delivery at the moment."

    def order_preparation_time(self):
        return "It will take just 5 minutes more"
    def food_options(self):
        return "Our menu includes pizza, burgers, sandwiches, salads, and pasta."

    def payment_options(self):
        return "We accept cash, credit/debit cards, and online payment methods."

    def discounts(self):
        return "there is 10% off on today's special"
    def leave_feedback(self):
        return "You can leave feedback by contacting our customer support phone# 03000000000 or filling out our online survey.'Link'"

    def get_recommendation(self, user_input):
        for intent, questions in self.recommended_questions.items():
            if self.check_intent(user_input, questions):
                return random.choice(questions)
        return random.choice(self.recommended_questions["default"])

    def conversation(self):
        print("Welcome to the Food Order Chatbot!")
        print("You can start chatting. Type 'bye' to exit.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("Bot:", self.respond(user_input))
                break
            else:
                print("Bot:", self.respond(user_input))

if __name__ == "__main__":
    chatbot = FoodOrderChatbot()
    chatbot.conversation()

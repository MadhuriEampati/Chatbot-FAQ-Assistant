from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging

class SimpleChatBot:
    def __init__(self):
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        
        # Create chatbot instance
        self.bot = ChatBot(
            'FAQ Assistant',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3',
            logic_adapters=[
                'chatterbot.logic.BestMatch',
                'chatterbot.logic.MathematicalEvaluation'
            ]
        )
        
        # Initialize trainer
        self.trainer = ListTrainer(self.bot)
        
        # Custom training data
        self.train_chatbot()

    def train_chatbot(self):
        # Define a list of questions and answers
        conversation = [
            "Hello",
            "Hi there!",
            "What is your name?",
            "My name is FAQ Assistant.",
            "What can you do?",
            "I can answer questions, have conversations, and provide information.",
            "Who created you?",
            "I was created by a Python developer using ChatterBot.",
            "How can I exit?",
            "Type 'exit' or 'quit' to end our conversation.",
            "What's your purpose?",
            "My purpose is to assist and have friendly conversations.",
            "Tell me about AI.",
            "AI stands for Artificial Intelligence, which refers to machines designed to perform tasks that typically require human intelligence.",
            "What language are you written in?",
            "I'm written in Python using the ChatterBot library."
        ]
        
        # Train the chatbot with the custom conversation
        self.trainer.train(conversation)

    def start(self):
        print("\nFAQ Assistant: Hello! I'm your FAQ Assistant. How can I help you today?")
        print("Type 'exit' or 'quit' to end the conversation.\n")
        
        while True:
            try:
                user_input = input("You: ")
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print("FAQ Assistant: Goodbye! Have a great day!")
                    break
                    
                response = self.bot.get_response(user_input)
                print("FAQ Assistant:", response)
                
            except (KeyboardInterrupt, EOFError, SystemExit):
                print("\nFAQ Assistant: Session ended. Goodbye!")
                break
            except Exception as e:
                print("Error occurred:", str(e))
                continue

if __name__ == "__main__":
    chatbot = SimpleChatBot()
    chatbot.start()

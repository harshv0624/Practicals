from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on English language data
trainer.train('chatterbot.corpus.english')

# Start the conversation loop
print("Chatbot: Hello! How can I help you today? (Type 'exit' to end)")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    response = chatbot.get_response(user_input)
    print("Chatbot:", response)

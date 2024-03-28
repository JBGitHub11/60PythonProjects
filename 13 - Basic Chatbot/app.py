import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)|i am (.*)|i'm (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name?|who are you?|what are you?",
        ["My name is ChatBot"]
    ],
    [
        r"how are you?|how are you doing?|what's up?",
        ["I'm doing well, thanks for asking!"]
    ],
    [
        r"quit|bye|goodbye",
        ["Bye! Take care."]
    ],
    [
        r"(.*)|",
        ["I don't understand, can you rephrase your question?"]
    ]
]

# Create a ChatBot instance
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hello, I am a chatbot. Let's chat!")
chatbot.converse()
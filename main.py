# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the Chatbot class for interaction.
class ChatBot:
    def __init__(self):

        # Initializing the sentiment analysis tool.
        self.sentiment_analyzer = TextBlob("")
    def start_chat(self):
        print("ChatBot: Hi, how can I help you?")
        while True:
            user_message = input("You: ").strip()
            # Analyzing the sentiment of the user's message.
            self.sentiment_analyzer = TextBlob(user_message)
            sentiment_score = self.sentiment_analyzer.sentiment.polarity
            # Generating the chatbot's response based on sentiment.
            if sentiment_score > 0:
                chatbot_message = (f"ChatBot: That's great to hear! "
                                   f"\n Sentiment Score: {sentiment_score}")
            elif sentiment_score < 0:
                chatbot_message = (f"\nChatbot: I'm sorry to hear that. Would you like me to transfer you to a "
                                   f"live agent?"
                                   f"\n Sentiment Score: {sentiment_score}")
            else:
                chatbot_message = (f"\nChatbot: Hmm, I see. Can you please provide more information?"
                                   f"\n Sentiment Score: {sentiment_score}")

            # Printing the chatbot's response and sentiment
            print(chatbot_message)
if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.start_chat()


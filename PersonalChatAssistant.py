import datetime
import time
name = input("Please enter your name: ")
presentHour = datetime.datetime.now().hour
if 5<= presentHour < 12:
    print(f"Good Morning {name}!")
elif 12 <= presentHour < 18:
    print(f"Good Afternoon {name}!")
else:
    print(f"Good Evening {name}!")
print(f"Hi {name}, I am a bot created by suju!")
print("Ask me questions and say exit to end the convo")
#giving memrory to the bot
responses = {
    "hi": "Hello! How can I assist you today?",
    "how are you?": "Fine baby! I'm just a bot, but I'm here to help you!",
    "what's your name?": "I am a Personal Chat Assistant created by suju.",
    "exit": "Goodbye! Have a great day!"
}
#function to get response
def getResponse(userInput):
    userInput = userInput.lower() #convert to lowercase for 
    for eachKey in responses:
        if eachKey in userInput:
            return responses[eachKey]
    return "Sorry, I don't have answer for that!"

#Take user input
while True:
    userInput = input("Please ask me a qn: ")
    reply = getResponse(userInput)
    print("Bot:" +reply)
    if "exit" in userInput.lower():
        break

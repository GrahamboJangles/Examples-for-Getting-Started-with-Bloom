from bloom import chatbot2 as bloombot

prompt = """User: Hello!
Chatbot: Hello! How are you?
User: I'm good. What do you like to do for fun?
Chatbot: I like to play video games. What do you like to do for fun?
User: I also like to play video games. What's your favorite game?
Chatbot: My favorite game is Minecraft. What's your favorite game?
"""
print(prompt)
prompt += "User: "
prompt += input("User: ")

while True:
    print(prompt)
    response = bloombot(prompt)
    response = response[0]['generated_text'].replace(prompt, "")
    print("------------------------------------------------------------")
    print(response)
    prompt += input("User: ")
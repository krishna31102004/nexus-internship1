# greeting function
def greeting():
    return "Hello! How may I assist you today?"
# farewell function
def farewell():
    return "Bye-bye! Have a nice day!"
# responses to questions function
def answers_to_questions(question):
    responses = {
        "what is the capital of india?": "New Delhi",
        "how many states are there in india?": "28",
        "how are you?": "Hello! I'm a chatbot, so I don't have feelings, but I'm here to assist you. How can I help you today?",
        "what is the population of the world?": "8.1 billion",
        "what programming language has been used to code you in?": "Python"
    }
# converting all questions to lower case
    return responses.get(question.lower(), "I'm sorry, I do not understand that question.")

# to remember the previous interactions
conversation_history = {}


# to ensure all the previous interactions are being saved
def prev_interactions(user, response):
    if user not in conversation_history:
        conversation_history[user] = []
    conversation_history[user].append(response)

# function to recall context
def recall_context(user):
    if user in conversation_history:
        return "If I recall, we talked about: " + ", ".join(conversation_history[user])
    else:
        return "This is the first I am hearing about it."


# chatbot asking the user some questions
def ask_user_questions(user):
    questions = [
        "What's your favorite sport?",
        "What's your favorite programming language?",
        "Do you like the weather today?"
    ]
    answers = []
    for question in questions:
        print(question)
        answer = input("You: ")
        answers.append(answer)
        prev_interactions(user, question + " " + answer)
    return answers

# error handling function
def error_handle():
    return "Apologies but I did not quite get that. Could you please rephrase your statement?"

# main function
def main():
    user = "person"
    print("Chatbot: " + greeting())
    prev_interactions(user, "User greeted")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: " + farewell())
            prev_interactions(user, "Said goodbye to user")
            break
        elif user_input.lower() in ["recall", "context"]:
            print("Chatbot: " + recall_context(user))
        elif user_input.lower() == "ask me something":
            answers = ask_user_questions(user)
            print("Chatbot: That's interesting! Thank you for sharing that!")
            prev_interactions(user, "User answered: " + ", ".join(answers))
        else:
            response = answers_to_questions(user_input)
            if response == "I'm sorry, I do not understand that question.":
                print("Chatbot: " + error_handle())
            else:
                print("Chatbot: " + response)
                prev_interactions(user, "Question asked: " + user_input + " | Responded with: " + response)

if __name__ == "__main__":
    main()
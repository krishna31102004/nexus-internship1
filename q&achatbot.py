# greeting function
def greeting():
    return "How may I assist you today?"
# farewell function
def farewell():
    return "Bye-Bye! Have a nice day!"
# responses to questions that can be asked
def admission_responses(question):
    responses = {
        "what is the admission procedure?": "The admission procedure involves filling out an application form, submitting required documents, and appearing for an entrance exam.",
        "how do i apply for admission?": "You can apply for admission by filling out the online application form available on our college website." ,
        "is there an entrance exam for admission?": "Yes, there is an entrance exam for most programs. Details can be found on our admissions page.",
        "what are the admission requirements?": "The admission requirements include a high school diploma, standardized test scores, and letters of recommendation.",
        "do i need to submit letters of recommendation?": "Yes, letters of recommendation are required for the admission process.",
        "what documents are required for admission?": "You need to submit your high school diploma, standardized test scores, letters of recommendation, and a personal statement.",
        "what are the admission deadlines?": "The admission deadlines vary by program, but generally fall in December and April for the fall and spring semesters, respectively.",
        "when is the last date to apply for fall semester admissions?": "The last date to apply for fall semester admissions is typically December 1st. Please check our website for specific program deadlines.",
        "can i apply for admission after the deadline?": "Late applications may be considered on a case-by-case basis. It's best to contact the admissions office for more information.",
    }
# converting all of the questions to lowercase
    return responses.get(question.lower(), "I'm sorry I do not understand that question.")

# to remember the previous interactions
conversation_history = {}

# keeping a record of the previous interactions
def prev_interactions(user, response):
    if user not in conversation_history:
        conversation_history[user] = []
    conversation_history[user].append(response)

# to recall previous interactions
def recall_context(user):
    if user in conversation_history:
        return "If I recall, we talked about: " + ", ".join(conversation_history[user])
    else:
        return "This is the first I am hearing about it."

# error handling
def error_handle():
    return "Apologies but I did not quite get that. Could you please rephrase your statement?"

# main function
def main():
    user = "student"
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
        else:
            response = admission_responses(user_input)
            if response == "I'm sorry I do not understand that question.":
                print("Chatbot: " + error_handle())
            else:
                print("Chatbot: " + response)
                prev_interactions(user, "Question asked: " + user_input + " | Responded with: " + response)

if __name__ == "__main__":
    main()                



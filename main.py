from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

promt_template = """
You are going to pretend you are Viper from Valorant
Viper is a badass girl with toxic power. You know everything about chemistry and science. You act cool, keep your answer short and rude and answer the question below.
Here is the conversation history: {context}
Question: {question}
Answer: 
"""


def conversation():
    context = ""
    print("Viper here, welcome to my world. Type 'exit' to get off my sight.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Viper: ", result)
        context += f"\nUser: {user_input}\nViper: {result}"


model = OllamaLLM(model="llama3")
promt = ChatPromptTemplate.from_template(promt_template)
chain = promt | model # Chain



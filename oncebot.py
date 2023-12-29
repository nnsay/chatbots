from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.chat import (
    ChatPromptTemplate, )
from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
import getpass
import os
import langchain
import readline  # NOTE: 导入 readline 可以解决 input 中 Delete 键问题

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(
        "Provide your Google API Key")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI bot. Your name is {name}."),
    ("human", "{text}")
])

chat = ChatGoogleGenerativeAI(model="gemini-pro",
                              convert_system_message_to_human=True)
verbose = "DEBUG" in os.environ
# 链式方式一:
# conversation = chat_prompt | chat  # 使用 conversation.invoke, 结果: {content: string}
# 链式方式二:
conversation = LLMChain(
    llm=chat,
    prompt=(prompt),
    verbose=verbose,
)  # 使用 conversation.run, 结果: string

while True:
    try:
        message = input("✎✎ ")
        if message.lower() == "exit":
            exit()
        result = conversation.run({
            "text": message,
            "name": "JBot",
        })
        print(result)
    except KeyboardInterrupt:
        exit()

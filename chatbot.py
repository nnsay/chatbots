from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.chains import LLMChain, ConversationChain
from langchain.memory import ConversationBufferMemory
import getpass
import os
import langchain
import readline  # NOTE: 导入 readline 可以解决 input 中 Delete 键问题

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass(
        "Provide your Google API Key")

prompt = ChatPromptTemplate(messages=[
    SystemMessagePromptTemplate.from_template(
        "You are a nice chatbot having a conversation with a human."),
    # The `variable_name` here is what must align with memory
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
])

chat = ChatGoogleGenerativeAI(model="gemini-pro",
                              convert_system_message_to_human=True)

memory = ConversationBufferMemory(memory_key="chat_history",
                                  return_messages=True)
verbose = "DEBUG" in os.environ
# 链式方式一:
# conversation = chat_prompt | chat  # 使用 conversation.invoke, 结果: {content: string}
# 链式方式二:
conversation = LLMChain(llm=chat,
                        prompt=prompt,
                        verbose=verbose,
                        memory=memory)  # 使用 conversation, 结果: string

# conversation({"question": "讲个笑话"})
# conversation({"question": "不怎么好笑"})
# result = conversation({"question": "再说一个"})
# print(result)

while True:
    try:
        message = input("✎✎ ")
        result = conversation({
            "text": message,
        })
        print(result['text'])
    except KeyboardInterrupt:
        break
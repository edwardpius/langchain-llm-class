import os
import openai
from dotenv import find_dotenv, load_dotenv
from langchain.llms import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv(find_dotenv(filename='.env'))
openai.api_key = os.getenv("OPENAI_API_KEY")

llm_model = "gpt-3.5-turbo"

# prompt = "How old is the Universe"
# prompt = "What is the weather in WA DC"

# messages = [HumanMessage(content=prompt)]

llm = openai.OpenAI(temperature=0.7)

# llm = open(temperature=0.7)
# chat_model = ChatOpenAI(temperature=0.7)
# llm = ChatOpenAI(openai_api_key="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")

# print(chat_model.predict_messages(messages).content)
print(llm.predict("What is the weather in Seattle WA"))
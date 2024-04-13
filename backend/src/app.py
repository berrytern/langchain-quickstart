from src.models import TranslateModel, ChatInputModel, HumanMessageModel, AIMessageModel
from src.utils import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langserve import add_routes


app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


model = ChatOpenAI(api_key=settings.OPENAI_API_KEY)


@app.post("/translate")
async def translate(item: TranslateModel):
    #template = ChatPromptTemplate.from_template("Translate the following sentence to Portuguese: {item.sentence}")
    message = model.invoke([
        HumanMessage(content=f"Translate the following sentence to Portuguese: {item.sentence}")
    ])
    return {"message": message.content}


@app.post("/chat")
async def chat(chat_input: ChatInputModel):
    #template = ChatPromptTemplate.from_template("Translate the following sentence to Portuguese: {item.sentence}")
    input_messages = [
        *[HumanMessage(content=message["human"]) if "human" in message else AIMessage(content=message["ai"]) for message in chat_input.history],
        HumanMessage(content=chat_input.message)
    ]
    
    response = model.invoke(input_messages)
    mounted_response = [*chat_input.history, {"human":chat_input.message}, {"ai": response.content}]
    return mounted_response

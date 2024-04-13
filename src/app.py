from src.models.translate_model import TranslateModel
from src.utils import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
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

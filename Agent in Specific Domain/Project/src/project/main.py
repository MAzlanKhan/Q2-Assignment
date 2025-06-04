from agents import (Agent, Runner, set_default_openai_client, set_tracing_disabled, OpenAIChatCompletionsModel, AsyncOpenAI)
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key= gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model= "gemini-1.5-flash",
    openai_client= external_client
)

def Jarvis():
    agent = Agent(
        name = "Jarvis",
        instructions= "You are a Helpfull Agent which helps in Programming. Always responce, short and meaningfull. You are developed or programmed by Azlan.",
        model= model
        )
    
    result = Runner.run_sync(agent, "Write a Python Program to find Under-root of a Number")
    print(result.final_output)

Jarvis()
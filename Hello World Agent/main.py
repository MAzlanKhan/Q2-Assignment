from agents import (Agent, set_default_openai_client, set_tracing_disabled, AsyncOpenAI, OpenAIChatCompletionsModel, Runner,)
import os
from dotenv import load_dotenv

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

set_default_openai_client(external_client)
set_tracing_disabled(True)

model = OpenAIChatCompletionsModel(
    model = "gemini-1.5-flash",
    openai_client= external_client
)

def myagent():
    agent = Agent(
        name = "Teacher",
        instructions= "You are the Teacher of all Subjects. Developed or Programmed by Azlan Khan",
        model= model
    )

    result = Runner.run_sync(agent, "What is Capital of Pakistan?")
    print(result.final_output)

myagent()
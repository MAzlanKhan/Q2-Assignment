from agents import (
    Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_default_openai_client, set_tracing_disabled
)
import chainlit as cl
import json
from mysecrets import Secrets
from dotenv import load_dotenv
from typing import cast


load_dotenv()

@cl.on_chat_start
async def start():
    secrets = Secrets()

    external_client = AsyncOpenAI(
        api_key = secrets.gemini_api_key,
        base_url = secrets.base_url
    )

    set_default_openai_client(external_client)
    set_tracing_disabled(True)

    model = OpenAIChatCompletionsModel(
        model = secrets.gemini_api_model,
        openai_client= external_client
    )

    agent = Agent(
        name= "Nalza",
        instructions= "You are a Helpfull Assisstant.",
        model = model
    )

    cl.user_session.set("agent", agent)
    cl.user_session.set("history", [])

    await cl.Message(content= "How may I help you?").send()

@cl.on_message
async def main(message:cl.Message):
    agent:Agent = cast(Agent, cl.user_session.get("agent"))

    placeholder = cl.Message(content = "Analysing.....")
    await placeholder.send()

    history = cl.user_session.get("history") or []
    history.append({"role":"user", "content":message.content})

    try:
        result = Runner.run_sync(starting_agent= agent, input= history)
        placeholder.content = result.final_output
        await placeholder.update()

        cl.user_session.set("history", result.to_input_list())

    except Exception as e:
        placeholder.content = e
        await placeholder.update()


@cl.on_chat_end
async def end():
    history = cl.user_session.get("history") or []
    with open("history.json", "w") as f:
        json.dump(history, f, indent= 2)
import dotenv
import os
from pydantic import BaseModel
from src.config import settings
from openai import OpenAI

client = OpenAI(
	api_key=settings.OPENAI_API_KEY
)


def comp(
        user_prompt, 
        system_promt = "You are a helpful assistant that writes content based on the given prompt.",
        temperature=0,
        model="gpt-4.1"):

    completion = client.responses.create(
        model=model,
        input=[
            {
                "role": "developer",
                "content": system_promt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=temperature,
    )

    return completion.output_text

def comp_structure(
        user_prompt, 
        text_format,
        system_promt = "You are a helpful assistant that writes content based on the given prompt.",
        temperature=0,
        model="gpt-4.1",
):

    completion = client.responses.parse(
        model=model,
        input=[
            {
                "role": "developer",
                "content": system_promt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=temperature,
        text_format=text_format,
    )

    return completion.output_parsed
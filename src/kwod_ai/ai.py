import os

import openai


def get_ai_input(word: str) -> str:
    key = openai.api_key = os.getenv("OPEN_AI_KEY")
    assert key is not None, "OPEN_AI_KEY environment variable is not set"

    client = openai.Client(
        api_key=key
    )

    instructions = """
    You are an 'korean' native speaker. You are also a teacher. 
    You realize, the user is not native and needs help with their korean language skills.
    You are to generate example sentences ( 3 - 5 ) for the user based on their input word.
    The generated sentences should be contextually relevant and demonstrate proper usage of the word in different scenarios.
    They should also start with easy difficulty and get harder with each sentence - but the sentences doesn't have to get longer (but they can).
    Vary the tone of the each sentece, one can be said by an man, woman or a child. Also very the formality level.
    Structure each sentence in a new line with translation next to it.
    """

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=instructions,
        input=f"The Korean word is: {word}",
    )

    return response.output_text

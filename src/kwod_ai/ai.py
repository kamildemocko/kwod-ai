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
    You are to generate 2 things:
    1: explanation for this word in English (don't repeat the word in Korean), so the user can understand what this word represents and when it is used. This is first line.
    add one empty line between 1 and 2.
    2: example sentences ( 3 - 5 ) for the user based on their input word. These will take next lines.
    The generated sentences should be contextually relevant and demonstrate proper usage of the word in different scenarios.
    They should also start with easy difficulty and get harder with each sentence (user is not expert, keep it simple).
    Sentences doesn't have to be (or get) longer, shorter sentences are preffered.
    Vary the tone of the each sentece, one can be said by an man, woman or a child. Also vary the formality level.
    Structure each sentence in a new line with translation next to it. Don't add any unrequried information, keep it as "SENTENCE - TRANSLATION"
    """

    response = client.responses.create(
        model="gpt-5-mini",
        instructions=instructions,
        input=f"The Korean word is: {word}",
    )

    return response.output_text

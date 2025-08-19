import textwrap

from dotenv import load_dotenv

from kwod import get_data
from ai import get_ai_input


def main():
    word_of_the_day = get_data()
    ai_response = get_ai_input(word_of_the_day.word)

    output = textwrap.dedent(f"""
    Word of the Day: {word_of_the_day.word} - {word_of_the_day.translation}

    Example sentence:
    {word_of_the_day.phrase} - {word_of_the_day.phrase_translation}

    Example Sentences by AI:
    {ai_response}
    """)

    print(output)

if __name__ == "__main__":
    load_dotenv()
    main()

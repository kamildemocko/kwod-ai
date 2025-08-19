import textwrap

from dotenv import load_dotenv

from kwod import get_data
from ai import get_ai_input
from discord import send_message


def main():
    print("getting korean word of the day...")
    word_of_the_day = get_data()

    print("getting AI sentences...")
    ai_response = get_ai_input(word_of_the_day.word)

    output = textwrap.dedent(f"""
    Word of the Day: {word_of_the_day.word} - {word_of_the_day.translation}

    {textwrap.indent(ai_response, '    ')[3:]}

    Original example sentence:
    {word_of_the_day.phrase} - {word_of_the_day.phrase_translation}
    """)

    print("sending discord message...")
    send_message(output)

    print("all done")

if __name__ == "__main__":
    load_dotenv()
    main()

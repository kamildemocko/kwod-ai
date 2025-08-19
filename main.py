from string import Template

import httpx
from selectolax.parser import HTMLParser
import arrow


URL = Template("https://wotd.transparent.com/rss/$month-$day-$year-korean-widget.xml?t=$timestamp")


def main():
    with httpx.Client() as client:
        now = arrow.now()

        response = client.get(URL.substitute(
            timestamp=now.int_timestamp,
            year=now.format("YYYY"),
            month=now.format("MM"),
            day=now.format("DD"),
        ))
        response.raise_for_status()

        tree = HTMLParser(response.text)
        word_css = tree.css_first("word")
        word_translation_css = tree.css_first("translation")
        phrase_css = tree.css_first("fnphrase")
        phrase_translation_css = tree.css_first("enphrase")

        assert (
            word_css is not None and word_translation_css is not None
            and phrase_css is not None and phrase_translation_css is not None
        )

        word = word_css.text()
        word_translation = word_translation_css.text()
        phrase = phrase_css.text()
        phrase_translation = phrase_translation_css.text()

        print(word, word_translation, phrase, phrase_translation)


if __name__ == "__main__":
    main()

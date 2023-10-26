"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, value, title, words, text):
        """Create story with words and template text."""
        self.value = value
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text. Answers should be in a dictionary"""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    "creature",
    "A Mysterious Creature",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    "zoo",
    "A Day at the Zoo",
    ["adjective", "noun", "verb, past tense", "adverb", "verb", "number"],
    """Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree. He {verb, past tense} {adverb} through the large tunnel that led to its enclosure. I wanted to {verb} after it, but I couldn't follow. The ${number} ticket was not worth."""
)

#list of stories
story_list = {story.value: story for story in [story, story2]}
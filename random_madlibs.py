import random

# Madlib templates
madlibs = [
    "Roses are {color}, violets are {color}, sugar is {adjective}, and so are you!",
    "The {adjective} {noun} {verb} over the lazy {plural_noun}.",
    "I like to {verb} with {noun1} and {noun2} in the {place}.",
    "The {animal} {verb} {adverb} through the {adjective} {place}."
]

def get_word(prompt):
    return input(prompt + ": ")

def create_madlib():
    template = random.choice(madlibs)
    words = {
        "color": get_word("Enter a color"),
        "adjective": get_word("Enter an adjective"),
        "noun": get_word("Enter a noun"),
        "verb": get_word("Enter a verb"),
        "plural_noun": get_word("Enter a plural noun"),
        "adverb": get_word("Enter an adverb"),
        "animal": get_word("Enter an animal"),
        "place": get_word("Enter a place")
    }
    return template.format(**words)

def main():
    print("Welcome to the Random Madlib Game!")
    madlib = create_madlib()
    print("\nYour madlib:\n" + madlib)

if __name__ == "__main__":
    main()

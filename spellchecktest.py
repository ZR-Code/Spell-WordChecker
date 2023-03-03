from textblob import TextBlob


def spell_check(checking):
    a = TextBlob(checking)
    print(a.correct())
text = input("what would you like to Spell check? ")

spell_check(text)
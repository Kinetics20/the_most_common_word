from common_word import most_common_word


def test_most_common_word_basic():
    assert most_common_word("Home is where I feel safe, but the house I grew up in will always be home to me.") == (
        'home', 2)

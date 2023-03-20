"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
   for item in items:
       print(item)


def get_all_evens(nums):
    return [x for x in nums if x % 2 == 0]

def get_odd_indices(items):
    return [y for x, y in enumerate(items) if x % 2 != 0]


def print_as_numbered_list(items):
    # i = 1

    # for item in items:
    #     print(f"{i}. {item}")
    #     i += 1

    for idx, item in enumerate(items):
        print(f"{idx+1}. {item}")
        


def get_range(start, stop):
    # return [num for num in range(start, stop)]
    return list(range(start, stop))


def censor_vowels(word):
    vowels = "aeiou"
    new_word = []

    for char in word:
        if char in vowels:
            char = "*"
        new_word.append(char)
    
    return "".join(new_word)

    # return [c for c if not c in vowels else "*" for c in word]



def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code

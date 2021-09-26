from itertools import combinations
import string

# # Init some peace of string
text = "A do run run, a do run run"
text.replace(" ", "")


def remove_punc(inp):
    output = ""

    for i in range(len(inp)):
        if inp[i].isalnum():
            output += inp[i]
    return output.lower()


# Test initial string
# Debug

mod = remove_punc(text)
print(mod)

# Init K
k = 5

# Init Hash K
hk = 2
# itertools.combinations() is an inbuilt function that gets  all K length aka the substrings from the string
# Extracting k-grams a.k.a k length substrings

res = [mod[x:y] for x, y in combinations(
    range(len(mod) + 1), r=2) if len(mod[x:y]) == k]

print(res)
# Hash through the tuple
res_hash = hash(tuple(res))
# Change int to string

hashed_string = str(res_hash)
print(hashed_string)
h_res = [hashed_string[x:y] for x, y in combinations(
    range(len(hashed_string) + 1), r=2) if len(hashed_string[x:y]) == hk]
print(h_res)

# TODO :  Create a window of hashes in a tuple strcture


# Once more find a string that works with 0 mod p where p is fixed


#

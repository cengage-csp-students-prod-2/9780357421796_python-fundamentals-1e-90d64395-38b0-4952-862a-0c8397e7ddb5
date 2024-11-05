# Write your code here
def word_counter(sentence):
    result = {}
    for char in sentence:
        if char != " ":
            if char in result:
                result[char] += 1
            else:
                result[char] = 1
    return result
           
print(word_counter("Mississippi"))
# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, list):
        new_list = []
        for item in list:
            if sorted([letter for letter in item]) == sorted([letter for letter in self.word]):
                new_list.append(item)
        return new_list

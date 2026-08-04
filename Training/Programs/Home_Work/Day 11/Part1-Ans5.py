# sentence= input("Enter a sentence:")
def count_unique_words(sentence):
    my_list=sentence.lower().split(" ")
    y=set(my_list)
    return len(y)
sentence= input("Enter a sentence:")
count=count_unique_words(sentence)
print(f"You used {count} unique words")
    
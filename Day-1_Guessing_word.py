word = "pallavi"
guessing_word = ""
guessing_count = 0
guessing_limit = 5
out_of_guessing = False


while guessing_word != word and not(out_of_guessing):
    if guessing_limit > guessing_count:
        guessing_word = input("enter guessing word: ")
        guessing_count += 1
    else:
        out_of_guessing = True
if out_of_guessing:
    print("limit is out of guessing, You are fail !")
else:    
    print("You are win!")
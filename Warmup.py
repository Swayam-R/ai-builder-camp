def rank_message():
    name = input("Enter your name: ")
    rank = input("Enter your rocket league rank: ")
    return name + " is currently " + rank

print("Greetings, " + rank_message())
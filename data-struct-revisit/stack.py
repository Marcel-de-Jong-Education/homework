stack = []

print("Simple text editor (type words, type 'undo' to remove last word, 'quit' to exit)! <3\n")

while True:
    word = input("Type a word: ")

    if word.lower() == "quit":
        print("Exiting editor.")
        break

    elif word.lower() == "undo":
        if stack:
            removed = stack.pop()
            print(f"Removed: {removed}")
        else:
            print("Nothing to undo.")

    else:
        stack.append(word)

    print("Current sentence:", " ".join(stack))

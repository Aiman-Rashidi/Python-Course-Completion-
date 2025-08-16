word_count = 0
while (line := input("enter: ").strip().lower()) != "done":
    word_count += len(line.split())
print(f"word count: {word_count}")
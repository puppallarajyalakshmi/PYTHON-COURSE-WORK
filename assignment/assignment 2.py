# Get input
num_messages = int(input("Enter the number of messages: "))
messages = []
users = {}

for _ in range(num_messages):
    msg = input()
    messages.append(msg)
    if ':' in msg:
        name, content = msg.split(':', 1)
        name = name.strip()
        content = content.strip()
        if name not in users:
            users[name] = []
        users[name].append(content)

# Menu loop
while True:
    print("\nChoose an analysis option (1–19, 0 to exit):")
    print("1. Count total messages")
    print("2. Show unique users")
    print("3. Count total words")
    print("4. Average words per message")
    print("5. Find longest message")
    print("6. Most active user")
    print("7. Message count by user")
    print("8. Most frequent word by user")
    print("9. First and last message by user")
    print("10. Check if user is present")
    print("11. Common repeated words")
    print("12. Total characters in chat")
    print("13. User with longest average message")
    print("14. Messages mentioning a user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract questions")
    print("18. Reply ratio between users")
    print("19. Count deleted messages")
    print("0. Exit")

    try:
        choice = int(input("Enter choice: "))
    except:
        print("Invalid input.")
        continue

    if choice == 0:
        break

    elif choice == 1:
        print("Total messages:", len(messages))

    elif choice == 2:
        print("Unique users in the chat:", list(users.keys()))

    elif choice == 3:
        total_words = 0
        for msg in messages:
            total_words += len(msg.split())
        print("Total words in the chat:", total_words)

    elif choice == 4:
        total_words = 0
        for msg in messages:
            total_words += len(msg.split())
        avg = total_words / len(messages)
        print("Average words per message:", round(avg, 2))

    elif choice == 5:
        longest = ""
        for msg in messages:
            if len(msg) > len(longest):
                longest = msg
        print("Longest message:", '"' + longest + '"')

    elif choice == 6:
        max_user = ""
        max_count = 0
        for user in users:
            count = len(users[user])
            if count > max_count:
                max_count = count
                max_user = user
        print("Most active user:", max_user, f"({max_count} messages)")

    elif choice == 7:
        name = input("Enter username: ").strip()
        print(f"Messages sent by {name}: {len(users.get(name, []))}")

    elif choice == 8:
        name = input("Enter username: ").strip()
        if name in users:
            word_counts = {}
            all_words = " ".join(users[name]).lower().split()
            for word in all_words:
                if word not in word_counts:
                    word_counts[word] = 0
                word_counts[word] += 1
            max_word = ""
            max_count = 0
            for word in word_counts:
                if word_counts[word] > max_count:
                    max_count = word_counts[word]
                    max_word = word
            if max_word != "":
                print(f"Most frequent word used by {name}: \"{max_word}\"")
            else:
                print("No words found.")
        else:
            print(f"User '{name}' not found.")

    elif choice == 9:
        name = input("Enter username: ").strip()
        first = ""
        last = ""
        for msg in messages:
            if msg.startswith(name + ":"):
                if first == "":
                    first = msg
                last = msg
        if first:
            print(f"First message by {name}: \"{first}\"")
            print(f"Last message by {name}: \"{last}\"")
        else:
            print(f"No messages by {name} found.")

    elif choice == 10:
        name = input("Enter username: ").strip()
        if name in users:
            print(f"User '{name}' found in the chat.")
        else:
            print(f"User '{name}' not found.")

    elif choice == 11:
        word_counts = {}
        for msg in messages:
            if ":" in msg:
                content = msg.split(":", 1)[1]
                words = content.lower().split()
                for word in words:
                    if word not in word_counts:
                        word_counts[word] = 0
                    word_counts[word] += 1
        repeated = []
        for word in word_counts:
            if word_counts[word] > 1:
                repeated.append(word)
        print("Common repeated words:", repeated)

    elif choice == 12:
        total_chars = 0
        for msg in messages:
            total_chars += len(msg)
        print("Total characters in chat:", total_chars)

    elif choice == 13:
        max_user = ""
        max_avg = 0
        for user in users:
            word_total = 0
            for msg in users[user]:
                word_total += len(msg.split())
            avg = word_total / len(users[user])
            if avg > max_avg:
                max_avg = avg
                max_user = user
        print(f"User with longest average message: {max_user} (avg {round(max_avg, 2)} words)")

    elif choice == 14:
        name = input("Enter name to search mentions: ").strip().lower()
        count = 0
        for msg in messages:
            if name in msg.lower():
                count += 1
        print(f"Messages mentioning '{name}': {count}")

    elif choice == 15:
        unique_msgs = []
        for msg in messages:
            if msg not in unique_msgs:
                unique_msgs.append(msg)
        print(f"Unique messages count: {len(unique_msgs)}")

    elif choice == 16:
        for msg in sorted(messages):
            print(msg)

    elif choice == 17:
        print("Questions asked in the chat:")
        for msg in messages:
            if '?' in msg:
                print(msg)

    elif choice == 18:
        u1 = input("Enter sender user: ").strip()
        u2 = input("Enter reply user: ").strip()
        count = 0
        for i in range(1, len(messages)):
            if messages[i - 1].startswith(u1 + ":") and messages[i].startswith(u2 + ":"):
                count += 1
        print(f"Reply ratio from {u2} to {u1}: {count} replies")

    elif choice == 19:
        deleted = 0
        for msg in messages:
            if "This message was deleted" in msg:
                deleted += 1
        print(f"Deleted messages found: {deleted}")

    else:
        print("Invalid choice. Try again.")
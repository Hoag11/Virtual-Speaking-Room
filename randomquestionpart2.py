import random
import re


def choose_random_topic(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        topics = file.read().split('\n\n')  # Assuming topics are separated by double newline

    chosen_topic = random.choice(topics).strip()

    # Use regular expression to find content within []
    matches = re.findall(r'\[([^]]+)\]', chosen_topic)
    if matches:
        return matches[0]  # Return the first match found
    else:
        return None  # Handle case where [] not found


file_path = 'part2.txt'
print(choose_random_topic(file_path))

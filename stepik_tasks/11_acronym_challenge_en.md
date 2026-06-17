# 🔤 Acronym Challenge

A small Python console game.

The program generates a random three-letter acronym using Russian alphabet letters. The player's goal is to enter three words whose first letters match the generated acronym.

For example, if the program generates:

```text
KBS
```

The player could enter:

```text
Cat
Bird
Sun
```

If the first letters match the generated acronym, the player wins.

## What I practiced

- Working with strings
- Accessing the first character of a string
- Converting text to uppercase with `upper()`
- Generating random characters with `random.choice()`
- Using loops
- Building strings step by step from user input

## Interesting part

My first solution used three separate checks for three separate words.

Later, I refactored the code so that the program builds the player's acronym inside a loop and compares the final result. This approach makes the code shorter, cleaner, and easier to extend.

## Code

```python
import random

abbreviation = ''

for _ in range(3):
    generated_letter = random.choice("АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ")
    abbreviation += generated_letter

print(abbreviation)

player_abbreviation = ''

for _ in range(3):
    player_word = input().strip()
    player_abbreviation += player_word[0].upper()

if player_abbreviation == abbreviation:
    print("Oh mighty player! Only 1% of people knew this!")
else:
    print("Even the great ones make mistakes sometimes.")
```

--- 

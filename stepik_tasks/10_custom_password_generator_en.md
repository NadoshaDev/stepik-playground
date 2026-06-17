# 🔐 Custom Password Generator

A simple Python console password generator.

The user can customize which characters may appear in the password. By default, only lowercase English letters are used, but numbers and special characters can also be included.

After the user selects the desired options, the program generates a random 8-character password.

## Configuration

The user answers two questions:

* Should numbers be included?
* Should special characters be included?

Based on these choices, the program builds the allowed character set and generates a password.

## What I practiced

* Working with strings
* Building strings step by step
* Using `random.choice()`
* Handling user preferences
* Simplifying conditional logic
* Expanding character sets with `+=`

## Interesting part

My first solution used several large conditional branches to handle every possible combination of user answers. Later I refactored the code and started building the allowed character set incrementally with `+=`.

This made the solution shorter, cleaner, and much easier to read.

---

## 🐍 Code
```python
import random

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_symbols = '*$@(!'                  
password = ''
allowed_characters = ''

use_numbers = input().strip().lower()            # Хочешь, чтобы в пароле могли быть цифры - да/нет
use_special_symbols = input().strip().lower()    # Хочешь, чтобы в пароле могли быть спец символы - да/нет

if use_numbers == 'да': 
    allowed_characters += numbers
    
if use_special_symbols == 'да':
   allowed_characters += special_symbols
    
for _ in range(8):
    password += random.choice(letters + allowed_characters)

print("Ваш случайный пароль:", password)

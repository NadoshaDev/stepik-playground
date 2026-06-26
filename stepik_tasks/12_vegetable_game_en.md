# 🥕 Vegetable Game

This project consists of four connected exercises from the Stepik course.

Each new exercise builds on the previous one, so what started as a simple learning task gradually turned into a small console game.

This idea is exactly what I liked most — instead of starting from scratch every time, I could keep improving an existing project step by step.

## 🌱 Version 1

The first version introduces Python's `random` module.

The program randomly selects vegetables and creates a small harvest.

```python
import random

ingredient = ['огурец', 'помидор', 'лук', 'перец']

my_vegetables = []

for _ in range(6):
    vegetable = random.choice(ingredient)
    my_vegetables.append(vegetable)
    print("Вы получили:", vegetable)

print("Мы собрали:", my_vegetables)
```

##  Version 2

The second version introduces winning combinations.

Instead of simply displaying random vegetables, the program now checks whether the player has collected one of the required combinations.

```python
for _ in range(6):
    vegetable = random.choice(ingredient)
    my_vegetables.append(vegetable)
    print("Вы получили:", vegetable)
    
print("Мы собрали:", my_vegetables)

cucumber_count = my_vegetables.count('огурец')
tomato_count = my_vegetables.count('помидор')
pepper_count = my_vegetables.count('перец')
onion_count = my_vegetables.count('лук')

first_combo = cucumber_count > 1  and tomato_count > 0
  
second_combo = (
  cucumber_count > 0 and tomato_count > 0 
  and pepper_count > 0 and onion_count > 0
  )
  
if first_combo or second_combo: 
    print("О великий игрок, вы повелитель овощей!")
    
else:                  
    print("Увы, вам не повезло!")
```

##  Version 3

The next step adds user interaction.

The player chooses one of three bags, each containing its own set of possible vegetables. This makes the game more interesting and varied.

```python
import random

my_vegetables = []

bag1 = 'огурец', 'помидор'              # мешок - из него может выпасть: огурец или помидор
bag2 = 'перец', 'лук'                  # мешок - из него может выпасть: перец или лук
bag3 = 'помидор', 'перец'               # мешок - из него может выпасть: помидор или перец

for _ in range(6):
    print("Наш текущий набор:", my_vegetables)
    
    selected_player = int(input())            # Номер мешка
    
    if selected_player == 1:
        vegetable = random.choice(bag1)
        
    elif selected_player == 2:
        vegetable = random.choice(bag2)
        
    else:
        vegetable = random.choice(bag3)
        
    print("Вы получили:", vegetable)
    my_vegetables.append(vegetable)
    
print("Мы собрали:", my_vegetables)
```

## 🛡 Version 4

This is the only part of the project that I decided to improve on my own.

While testing the program in Python IDLE, I accidentally pressed **Enter** without entering a number.

The program immediately raised an error.

That was the moment I realized that even a small educational program should provide at least basic protection against invalid user input.

Since this was just a Stepik exercise, I wanted the simplest possible solution without making the assignment unnecessarily complicated.

That's how I was introduced to `try / except` for the first time and added basic error handling so the program would no longer crash because of invalid input.

```python
import random

my_vegetables = []

bag1 = 'огурец', 'помидор'              # мешок - из него может выпасть: огурец или помидор
bag2 = 'перец', 'лук'                  # мешок - из него может выпасть: перец или лук
bag3 = 'помидор', 'перец'               # мешок - из него может выпасть: помидор или перец

for _ in range(6):
    print("Наш текущий набор:", my_vegetables)
          
    try: 
        selected_player = int(input())            # Номер мешка
    except ValueError:
        print("Нужно ввести число!")
        continue
          
    if selected_player == 1:
        vegetable = random.choice(bag1)
        
    elif selected_player == 2:
        vegetable = random.choice(bag2)
        
    elif selected_player == 3:
        vegetable = random.choice(bag3)
          
    else:
        print("Такого мешка нет!")
        continue
        
    print("Вы получили:", vegetable)
    my_vegetables.append(vegetable)
    
print("Мы собрали:", my_vegetables)

cucumber_count = my_vegetables.count('огурец')
tomato_count = my_vegetables.count('помидор')
pepper_count = my_vegetables.count('перец')
onion_count = my_vegetables.count('лук')

first_combo = cucumber_count > 2  and tomato_count > 0
  
second_combo = (
  cucumber_count > 0 and tomato_count > 0 
  and pepper_count > 0 and onion_count > 0
  )

third_combo = tomato_count > 1 and pepper_count > 1

combos = [
    first_combo,
    second_combo, 
    third_combo
] 

if any(combos): 
    print("О великий игрок, вы повелитель овощей!")
    
else:                  
    print("Увы, вам не повезло!")
```

Another small but exciting discovery happened while working on this project.

At first, the winning combination check looked like this:

`if first_combo or second_combo`

Later it became:

```python
if first_combo or second_combo or third_combo:
```

Then I started thinking:

> "What if one day there are five or even ten combinations? Will I have to keep adding another `or` every time?"

I began looking for a way to tell Python:

> "If **any** of these combinations is true..."

And with a smile, I discovered that Python has exactly the tool I was looking for:

```python
if any(combos):
```

It was one of those small moments that made me appreciate how elegant and thoughtfully designed Python really is.

---

This project is not about building a complex game.

For me, it became a small story of learning, where the most valuable part wasn't the number of lines of code, but the process of experimenting, solving problems, and making small discoveries that gradually change the way I think about programming.

---
## 💭 Personal Note

While learning Python, I've noticed something interesting about myself.

Most beginner exercises don't require input validation yet, and I completely understand that the course introduces new concepts step by step.

But I almost can't resist leaving a program completely unprotected.

Whenever I accidentally break my own program during testing, I immediately want to find the simplest solution that I can already understand and apply with my current level of knowledge.

At the time I created this project, we hadn't yet covered input validation, data validation, or proper error handling in the course. Everything used here comes from small pieces of knowledge that I picked up on my own by asking questions, experimenting, and gradually exploring new Python features.

I'm not trying to jump ahead or use advanced techniques that I don't fully understand yet. Instead, I enjoy finding small, practical solutions that match my current level of knowledge—solutions that I truly understand instead of simply copying.

I don't want to turn every small learning exercise into a large project. But if I already know a simple way to make a program a little more reliable and user-friendly, I always feel like giving it a try.

I'm beginning to realize that looking for edge cases, thinking about different user scenarios, and making programs a little more robust are gradually becoming part of the way I learn programming.

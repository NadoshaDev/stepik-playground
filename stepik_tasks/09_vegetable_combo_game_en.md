# 🥒 Vegetable Combo Game

A small Python console game.

The player collects random vegetables. After each draw, the program shows which vegetable was received, and at the end displays the complete collection.

But collecting vegetables is not enough. True masters know the secret combinations!

## Combo #1
- 2 cucumbers
- 1 tomato

## Combo #2
- 1 cucumber
- 1 tomato
- 1 pepper
- 1 onion

If the collected vegetables contain at least one combo, the player earns the title of Vegetable Master.

## What I practiced
- Working with lists (`list`)
- Adding elements with `append()`
- Counting items with `count()`
- Complex conditions using `and` and `or`
- Boolean variables (`first_combo`, `second_combo`)
- Breaking large conditions into readable logical blocks

## My thought process
At first, I tried to find a combo as a complete list inside another list. Later I realized that a combo is actually a set of requirements, not an object itself. Once I changed my thinking, the solution became much simpler and easier to read.

This was one of the first exercises where I actively used boolean variables to describe game logic.

---

## 🐍 Code
```python
import random

ingredient = ['огурец', 'помидор', 'лук', 'перец']
my_vegetables = []

for _ in range(6):
    vegetable = random.choice(ingredient)
    my_vegetables.append(vegetable)
    print("Вы получили:", vegetable)

print("Мы собрали:", my_vegetables)

cucumber_count = my_vegetables.count('огурец')
tomato_count = my_vegetables.count('помидор')
pepper_count = my_vegetables.count('перец')
onion_count = my_vegetables.count('лук')

first_combo = cucumber_count > 1 and tomato_count > 0
second_combo = (
  cucumber_count > 0 and tomato_count > 0
  and pepper_count > 0 and onion_count > 0
)

if first_combo or second_combo:
    print("О великий игрок, вы повелитель овощей!")
else:
    print("Увы, вам не повезло!")

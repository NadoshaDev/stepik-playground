# Filtering with List and Set: Practice & Insights

## Task

Given a list of animals, filter only selected ones.

```python
animals = ['слон', 'заяц', 'волк', 'лев',
           'заяц', 'слон', 'бобёр', 'волк',
           'жираф', 'кот', 'заяц', 'слон']
```

---

## How I approached this

Today I was solving practice tasks on Stepik and unexpectedly encountered a new concept — `set`.

It was not part of the main task, but I saw another solution using curly brackets and became curious.

This led me to explore:
- what `set` is
- how it differs from `list`
- how it affects performance
- how it can be applied in real code

---

## 1. Solution using only list

```python
target_animals = ['заяц', 'кот', 'слон']

filtered_animals = [
    animal for animal in animals
    if animal in target_animals
]

print(filtered_animals)
```

### What I understood:
- This is a **list comprehension**
- It keeps:
  - order
  - duplicates
- But membership check (`in`) is slower (linear search)

---

## 2. Solution using only set

```python
target_animals = {'заяц', 'кот', 'слон'}

filtered_animals = {
    animal for animal in animals
    if animal in target_animals
}

print(filtered_animals)
```

### What I understood:
- This is a **set comprehension**
- It:
  - removes duplicates automatically
  - does NOT preserve order
- Uses `.add()` internally
- Faster membership check

---

## 3. Combined approach (best balance)

```python
target_animals = {'заяц', 'кот', 'слон'}

filtered_animals = [
    animal for animal in animals
    if animal in target_animals
]

print(filtered_animals)
```

### Key idea:
- `set` → used for **fast checking**
- `list` → used for **storing result**

### Result:
- fast performance
- order preserved
- duplicates preserved

---

## Additional task: splitting data into two groups

I also solved a related problem — splitting data into two lists.

### Option 1 — one loop (efficient)

```python
filtered_animals = []
other_animals = []

selected_animals = {'заяц', 'кот', 'слон'}

for animal in animals:
    if animal in selected_animals:
        filtered_animals.append(animal)
    else:
        other_animals.append(animal)

print(filtered_animals)
print(other_animals)
```

### What I understood:
- Only **one pass** through the list
- More efficient for large datasets
- Clear control over logic

---

### Option 2 — list comprehension (clean but double pass)

```python
selected_animals = {'заяц', 'кот', 'слон'}

filtered_animals = [animal for animal in animals if animal in selected_animals]
other_animals = [animal for animal in animals if animal not in selected_animals]

print(filtered_animals)
print(other_animals)
```

### What I understood:
- Code is shorter and cleaner
- But the list is processed **twice**
- Less efficient for large datasets

---

## Key insight from this comparison

There is no single "best" solution — it depends on the goal.

```text
Efficiency → use one loop (for)
Readability → use list comprehension
```

---

## Important discovery: set vs dict

During this task I discovered a confusing but important detail:

```python
{} → dict (not set)
```

### Examples:
```python
a = {}              # dict
a = set()           # empty set
a = {"кот", "заяц"}  # set
a = {"кот": 1}      # dict
```

### Key rule:
- `:` → dict
- no `:` → set
- empty `{}` → always dict

---

## Key insights from today

- `list` and `set` serve different purposes
- performance depends on data structure choice
- the same problem can be solved in multiple ways
- combining structures gives better results than using only one
- one-pass vs two-pass processing matters
- understanding "why" is more important than just writing code

---

## Final understanding

Instead of thinking:
```
list or set?
```

I now think:
```
where do I need speed?
where do I need order?
how many times do I process the data?
```

---

## Conclusion

This was not just a task solution, but a deeper understanding of:
- how Python data structures work together
- how to choose the right tool
- how to balance readability and performance
- how to write more efficient and maintainable code

This approach will be applied in my main project as well.

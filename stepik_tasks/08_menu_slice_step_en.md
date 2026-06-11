# Menu for Even and Odd Months

## What the program does

This program creates different restaurant menus depending on the month number.

For even months, it selects dishes with even indexes.

For odd months, it selects dishes with odd indexes.

## What I learned

The main topic of this task was list slicing.

I had already seen simple slices before, but this was my first time working with slices like:

```python
menu[0::2]
menu[1::2]
```

I learned that the third value in a slice is the step, which allows me to select every second element from a list.

## My "Aha!" Moment

At first, I solved the task using a regular `if` statement:

```python
if month % 2 != 0:
    result = menu[1::2]
else:
    result = menu[0::2]
```

Later, I found another student's solution:

```python
menu[month % 2::2]
```

My first reaction was:

> "What is this supposed to mean?" 😄

After breaking it down step by step, everything suddenly clicked.

I realized that:

* `month % 2` returns `0` for even months;
* `month % 2` returns `1` for odd months.

That value can be used directly as the starting index of the slice.

For me, this was one of those small Python tricks that look mysterious at first but become elegant once you understand them.

## What I liked

I enjoyed this task because it introduced a completely new idea.

A few weeks ago, this syntax would have looked like magic to me.

Now I can read it, understand it, and explain why it works.

Moments like this remind me how much progress I've already made while learning Python. 🚀


## 🐍 Code / Код

### Initial approach (через if/else)
```python
menu = ['Борщ', 'Салат Цезарь', 'Пицца Маргарита', 'Картофель фри',
        'Стейк', 'Рататуй', 'Чизкейк', 'Тирамису']

month = int(input())

if month % 2 != 0:
    result = menu[1::2]
else:
    result = menu[0::2]

print("Сегодня в меню:", result)
```

### Refactored approach (Pythonic slice)
```python
menu = ['Борщ', 'Салат Цезарь', 'Пицца Маргарита', 'Картофель фри',
        'Стейк', 'Рататуй', 'Чизкейк', 'Тирамису']

month = int(input())

result = menu[month % 2::2]

print("Сегодня в меню:", result)
```

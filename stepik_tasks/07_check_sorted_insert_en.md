# Task 07 — Check Sorted After Insert

## Goal

Insert a number into a sorted list and check whether the list remains sorted.

## What I practiced

* list.insert()
* range(len(list) - 1)
* comparing neighboring elements
* boolean flags
* break statement

## My thought process

At first, I tried to check sorting directly inside the loop and print the result immediately. The problem was that one correct comparison does not mean the entire list is sorted.

The key realization was that I needed to check all neighboring pairs and remember whether a violation had been found.

I also spent some time thinking about when it makes sense to stop checking. Once a single pair breaks the sorting order, there is no reason to continue. This made the `break` statement feel much more natural and useful.

## Reflection

The most interesting part of this task was understanding that algorithms often need a "state".

In this case, the boolean variable `is_sorted` stores information discovered during the loop.

This task also helped me better understand why we use:

range(len(list) - 1)

when comparing neighboring elements.

It felt like one of my first small algorithmic problems rather than a simple list exercise.

##  Code
```python
nums = [4, 15, 19, 35, 53, 64]

number = int(input())
index = int(input())

nums.insert(index, number)

is_sorted = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Сортировка сохранилась")
else:
    print("Список уже не отсортирован")

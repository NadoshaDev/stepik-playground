# NadoshaDev | Task 02: Фильтрация + сумма
nums = [3, 15, 8, 25, 40, 12, 7, 60]

start = int(input())
stop = int(input())

if start < 0:
  start = len(nums) + start
  
if stop < 0:
  stop = len(nums) + stop
  
if start <= stop:
  step = 1
  end = stop + 1
else:
  step = -1
  end = stop - 1

filtered_numbers = []
total = 0

for i in range(start, end, step):
  number = nums[i]
  if number > 10 and number % 5 == 0:
    filtered_numbers.append(number)
    total += number
    
print(total)    
    
# Альтернативный вариант (короче и быстрее)
# print(sum(filtered_numbers))

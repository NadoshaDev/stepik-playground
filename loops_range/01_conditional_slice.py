# NadoshaDev | 01. Диапазон и фильтрация
nums = [12, 7, 25, 40, 18, 3, 60, 22, 5]

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
for i in range(start, end, step):
  number = nums[i]
  if number > 10 and number % 5 == 0:
    filtered_numbers.append(number)
    
if filtered_numbers:  
  max_number = max(filtered_numbers)
else:
  print("ошибка")
  exit()
  
print(max_number)

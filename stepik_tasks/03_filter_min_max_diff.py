# NadoshaDev | Task 03: Разница min/max
nums = [12, 7, 25, 40, 18, 3, 60, 22, 5]

filtered_nums = []
for numb in nums:
  if numb > 10:
    filtered_nums.append(numb)

if filtered_nums:
  min_numb = min(filtered_nums)
  max_numb = max(filtered_nums)
  difference = max_numb - min_numb
else:
  print("список пуст")
  exit()

print(difference)  

# Ручной поиск (закомментирован для сравнения):
# min_numb = filtered_nums[0]
# max_numb = filtered_nums[0]
# for number in filtered_nums:
#     if number < min_numb:
#         min_numb = number
#     if number > max_numb:
#         max_numb = number
# difference = max_numb - min_numb
# print(difference)

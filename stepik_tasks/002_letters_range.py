letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З']
                  
start = int(input())              # Индекс буквы, с которой нужно начать
stop = int(input())               # Индекс буквы, на которой нужно закончить
step = int(input())               # Шаг = 1 или -1

if start < 0:
    start  = len(letters) + start
    
if stop < 0:
    stop = len(letters) + stop
    
if step == 1:
    end = stop + 1    
                  
elif step == -1:
    end = stop - 1
        
else:
    print("ошибка")
    exit()

for i in range(start, end, step):
    print(letters[i])

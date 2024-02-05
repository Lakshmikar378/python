def func(food):
    for i, x in enumerate(food):
        print(x, end=' ')
        if i < len(food) - 1:
            print(',', end=' ')
fruits = ['apple', 'banana', 'cherry']
func(fruits)
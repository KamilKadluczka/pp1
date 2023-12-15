def f(arr2D):
    points = 0
    for list_number in range(len(arr2D)):
        for i in arr2D[list_number]:
            x = arr2D[list_number][0]
            y = arr2D[list_number][1]
            
            if x > 0 and y > 0:
                points += 1
    return int(points / 2)

# # arr = [[1,4], [8,5]]
# arr = [[7,5],[4,-5],[1,9],[4,4]]

# print(f(arr))



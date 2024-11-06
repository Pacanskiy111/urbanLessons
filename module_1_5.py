immutable_var = ([1, 2], 123, "Hello", True)

# immutable_var[1] = 321 # Изменить не получится, потому что кортежи как константы - неизменяемые. В моём понимании :)
immutable_var[0][0] = 100 # Но внутри кортежа можно менять значения в массиве(списке). Также в моём понимании :)

mutable_list = [1, 2, 3, "Hello", False]
mutable_list[0] = 5
mutable_list[3] = "Bye"
print(f"Неизменяемый кортеж: {immutable_var}")
print(f"Изменяемый лист: {mutable_list}")
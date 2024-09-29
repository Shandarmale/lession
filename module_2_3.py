my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
null_is_nothing = 0
while null_is_nothing < len(my_list):
    if my_list[null_is_nothing] >= 0:
        if my_list[null_is_nothing] != 0:
            print(my_list[null_is_nothing])
            null_is_nothing = null_is_nothing + 1
            continue
        else:
            break

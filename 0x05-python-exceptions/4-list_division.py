#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                new_list.append(0)
            else:
                result = num1 / num2
                new_list.append(result)
        except ZeroDivisionError:
            print("Division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            pass
    return new_list

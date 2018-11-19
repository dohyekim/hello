s = "123x"

try:
    print(int(s) + 1)

except ValueError as ve:
    print("Error occurred!", ve)


finally:
    print("aaaaaa")
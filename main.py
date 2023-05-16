import math

PI = 3.14

def assign_one_value_to_multi_vars():
    x = y = z = 1
    return (x, y, z)

def assign_multi_values():
    try:
        x, y, z = 1, 2, 3
        print(f'{x=} {y=} {z=}')
    except ValueError:
        print('Cannot assign values to variables')
        
def unpack():
    fruits = ['🍎', '🍊', '🍒']
    apple, tangerine, cherry = fruits
    print(apple)
    print(tangerine)
    print(cherry)
    
def area(radius: int) -> float:
    return PI * math.pow(radius, 2)

def main():
    print(area(4))

if __name__ == '__main__':
    main()

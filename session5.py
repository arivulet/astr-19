import math

def main():
    
    entries =  1000
    
    beg = 0
    end = 2

    inc = 2 / (entries - 1)

    print("  x     sin(x)") 
    print("-" * 22)

    for i in range(entries):
        x = beg + i * inc
        sinx = math.sin(x)
        print(f"{x}     {sinx}")


if __name__ == "__main__":
    main()
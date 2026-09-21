def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day):
        if day > days:
            return

        print(f"Day {day}")
        count(day + 1)

    count(1)
    print("Harvest time!")

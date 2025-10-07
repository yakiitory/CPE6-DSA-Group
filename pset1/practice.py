from adt import LinkedList

def main():
    sllist = LinkedList()
    values = [1, 2, 3, 4, 5]
    for value in values:
        sllist.append(value)

    sllist.delete(4)

    list = sllist.to_list()
    print(*list, sep=", ")

if __name__ == "__main__":
    main()
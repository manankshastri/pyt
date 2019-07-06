def bubblesort(dataset):

    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp

        print("Current State: ", dataset)

def main():
    list1 = [20, 9, 8, 19, 78, 23, 57, 41, 49, 53]
    bubblesort(list1)
    print("Result: ", list1)


if __name__ == '__main__':
    main()

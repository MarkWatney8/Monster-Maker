from csv import writer


def to_file(file="monsters.csv", object=None):
    with open(file, "a", newline='\n') as f:
        if object:
            data = vars(object).values()
            write = writer(f)
            write.writerow(data)
        else:
            print("No object!")



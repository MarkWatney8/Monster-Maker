from csv import writer


def to_file(file="monsters.csv", object=None):
    with open(file, "a", newline='\n') as f:
        if object:
            data = vars(object).values()
            writer = writer(f)
            writer.writerow(data)
        else:
            print("No object!")



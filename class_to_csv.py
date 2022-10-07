from csv import writer


def to_file(file_name="monsters.csv", object=None):

    if object == None:
        print("No object!")
        return

    with open(file_name, "a") as file:
    
        object_parameters = vars(object).values()
        write = writer(file)
        write.writerow(object_parameters)

    file.close()





def add(array):
    return round(sum(array), max([len(str(i).split('.')[1]) for i in array]))
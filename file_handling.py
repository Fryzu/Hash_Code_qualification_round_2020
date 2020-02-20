from tqdm import tqdm


def read(file_name):
    with open('input/'+file_name, 'r') as f:
        rows, columns, num_vehicles, num_rides, bonus, steps = [int(x) for x in f.readline().split()]
        rides = (int(slices) for slices in tqdm(f.readline().split(), 'reading'))
    return capacity, pizzas


def write(file_name, data):
    types_count, selected_pizzas = data
    with open('output/'+file_name.replace('in', 'out'), 'w') as f:
        f.write(str(types_count) + '\n')
        for pizza in selected_pizzas:
            f.write(str(pizza) + ' ')


if __name__ == '__main__':
    capacity, pizzas = read('a_example.in')

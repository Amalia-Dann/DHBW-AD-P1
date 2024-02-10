def order(array):
    seq = list(array)
    ordered = [0] * len(array)
    for i in range(len(array)):
        max_index = 0
        for j in range(len(array)):
            if seq[j] > seq[max_index]:
                max_index = j
        seq[max_index] = float('-inf')
        ordered[i] = max_index
    return ordered


def main():
    # Eingabe
    capacity = 10.0
    weight = [6, 2, 2, 5]
    value = [5, 3, 6, 4]

    solution = [False] * len(weight)
    max_value = 0
    max_weight = 0

    density = [round(100 * v / w, 2) for v, w in zip(value, weight)]

    order_sequence = order(density)

    print("Gewicht:     ", weight)
    print("Wert:        ", value)
    print("Dichte:      ", density)
    print("Reihenfolge: ", order_sequence)
    print("\nLösung bei Kapazität von", capacity, "kg:")

    for i in range(len(weight)):
        if capacity - weight[order_sequence[i]] >= 0:
            max_weight += weight[order_sequence[i]]
            max_value += value[order_sequence[i]]
            capacity -= weight[order_sequence[i]]
            solution[order_sequence[i]] = True

    print(solution, "Maximalgewicht", max_weight, "Maximalwert", max_value)


if __name__ == "__main__":
    main()

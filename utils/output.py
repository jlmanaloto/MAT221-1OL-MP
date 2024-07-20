def out(data):
    columns_width = [
        max(len(str(item)) for item in col)
        for col in zip(*data)
    ]

    for row in data:
        print(" | ".join(
            f"{item:<{width}}" for item, width in zip(row, columns_width))
        )
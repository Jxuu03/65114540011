from openpyxl import load_workbook

if __name__ == '__main__':
    wb = load_workbook('Me & My partner.xlsx')
    sheet = wb.active

    valid_pairs = []

    for row in sheet:
        values = [cell.value for cell in row]

        if values[1] is not None and values[2] is not None:
            pair = (values[1], values[2])

            if values[1] < values[2]:
                pair = (values[2], values[1])
            if pair not in valid_pairs:
                valid_pairs.append(pair)


    print(f"Total number of valid pairs: {len(valid_pairs)}")
    print(valid_pairs)
    
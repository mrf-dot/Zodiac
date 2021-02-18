from prettytable import PrettyTable
def to_int(message: str, *valids) -> int:
    """Turns input into a valid integer

    """
    while True:
        answer = input(message)
        try: answer = int(answer)
        except: continue
        if valids:
            if answer not in valids: continue
        return answer
def table_dict(head1, head2, cases: dict):
    """Formats a dictionary as a table

    """
    table = PrettyTable()
    table.field_names = [head1, head2]
    for x in cases:
        table.add_row([x, cases[x][0]])
    print(table)


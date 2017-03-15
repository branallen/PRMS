
def col_name(idx):
    return {
        0: 'time',
        1: 'cumulative seconds',
        2: 'self seconds',
        3: 'calls',
        4: 'self ms/call',
        5: 'total ms/call',
        6: 'name',
    }.get(idx, None)


BREAK_LINE = 'the percentage of the total running time of the'


def is_row(row):
    if len(row) != 7:
       return False

    for idx, col in enumerate(row):
        if idx < 6:
            try:
                float(col)
            except ValueError:
                return False
   
    return True


names = dict()
with open('gprof_out.txt', 'r') as f:
    name_cnt = 0
    for line in f:
        cols = [c.strip() for c in line.split()]
	if is_row(cols):
            names[cols[-1]]

        if BREAK_LINE in line:
            break
        

    print(name_cnt)
        

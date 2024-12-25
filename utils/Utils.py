def read_file(file_name: str):
    with open(file_name) as riddle_in:
        riddle_in = [line.rstrip("\n") for line in riddle_in.readlines()]
        return riddle_in
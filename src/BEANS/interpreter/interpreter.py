def parser(file_path: str) -> list:
    code = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line == '' or line[0] == '#':
                break
            code.append(line.split(' '))
    return code

print(parser("code.beans"))
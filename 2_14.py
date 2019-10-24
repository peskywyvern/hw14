# Write a function called new_lines that takes a file path, opens the file
# and adds a newline character (\n) once in 20 symbols


def new_lines(path: str):
    new_lines = []

    with open(path, 'r') as file:
        for line in file:
            if len(line) > 20:
                new_lines.append(line[:19] + '\n' + line[20:])
            else:
                new_lines.append(line)

    with open(path, 'w') as file:
        for line in new_lines:
            file.write(line)


new_lines('files/file2.txt')


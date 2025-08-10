import time

def write_to_pipe(pipe, message):
    with open(pipe, 'w') as file:
        file.write(message)

def read_pipe(pipe):
    with open(pipe, 'r') as file:
        return file.read()

def read_write_cycle(pipe, message):
    write_to_pipe(pipe, message)
    count = 0
    while count < 20:
        time.sleep(.5)
        content = read_pipe(pipe)
        if content != '' and content != message:
            return content
        count += 1
    return False
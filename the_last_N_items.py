
#keeping the last n element (in this case, the last 5)

from collections import deque

def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)



# example use on a File

if __name__ == '__main__':
    with open('me.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end="")
            print(line, end="")
            print('-'*20)
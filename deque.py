from collections import deque


# def search (lines, pattern, history=5):
#     previous_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, previous_lines
#         previous_lines.append(line)
        
        

# if __name__ == '__main__':
#     with open('me.txt') as f:
#         for line, prevlines in search(f, 'python', 5):
#             for pline in prevlines:
#                 print(pline, end='')
#             print(line, end='')
#             print('_'*20)
        


#basics of deque (DOUBLE END QUEUE)

q = deque([1,2,3])
q.appendleft(0)
print(q)
q.append(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)


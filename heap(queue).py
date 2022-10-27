import heapq

# nums = [1,9,76, 12, 98, 2,8,0,78,54,82,998]
# print(heapq.heappop(nums))
# print(nums)

# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# students = [
#     {"name": 'Sanusi Azeem', 'subjects': 10, 'score': 90},
#     {'name': 'Ajala Ruqiya', 'subjects': 12, 'score': 92},
#     {'name': 'Kawojue Raheem', 'subjects': 11, 'score': 78},
#     {'name': 'Quadri Wahab', 'subjects': 19, 'score': 23},
#     {'name': 'Micheal Jordan', 'subjects': 12, 'score': 23},
#     {'name': 'Messi Ronaldo', 'subjects': 9, 'score': 87},
#     {'name': 'Shanks Comics', 'subjects': 13, 'score': 69},
# ]

# highest = heapq.nlargest(3, students, key=lambda s:s['score'])
# print(highest)

class TodoPriority:
    def __init__(self) -> None:
        self.queue = []
        self.index = 0
    def push(self, todo, priority):
        # the index is after the priority in case two items have the same priority the index will be used to compare
        heapq.heappush(self.queue, (-priority,self.index , todo))
        self.index+=1
    def pop(self):
        return heapq.heappop(self.queue)[1]
        
        
class Todo:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self) -> str:
        return 'Todo({!r})'.format(self.name)
    
    
todo1 = TodoPriority()
todo1.push(Todo('eat'), 1)
todo1.push(Todo('code'), 2)
todo1.push(Todo('sleep'), 3)

print(todo1.pop())
print(todo1.queue)

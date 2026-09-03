x=[1,2,3,4]
y=iter(x)
print(y)
print(next(y))
print(next(y))

users=[
    {"id":1,"name":"A"},
    {"id":2,"name":"B"},
    {"id":3,"name":"C"},
    {"id":199,"name":"QQ"}
]

target=next((i for i in users if i["id"]==199))
print(target)
print(target["name"])

# +
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

counter = Countdown(3)
# print(next(counter))  # Output: 3

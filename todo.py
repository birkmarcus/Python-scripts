import os

os.system('clear')

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

def add_todo(item, list):
    todos.append(item)
    print("\n")
    os.system('clear')
    for i, item in enumerate(list, start=1):
        print(f"[{i}] ",item)

def close_todo(item, list):
    list[int(item)-1] = strike(list[int(item)-1])
    print("\n")
    os.system('clear')
    for i, item in enumerate(list, start=1):
        print(f"[{i}] ",item)

todos = []

if __name__ == "__main__":
    while True:
        done = input(f"->   ")
        if done.isnumeric():
            try:
                close_todo(done, todos)
            except:
                continue
        else:
            add_todo(done, todos)


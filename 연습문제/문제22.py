#문제 22번 문자열 역순
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(input_string):
    stack = Stack()

    # 문자열을 스택에 역순으로 저장
    for char in input_string:
        stack.push(char)

    reversed_string = ""

    # 스택에서 역순으로 문자열을 추출하여 문자열을 만듦
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

def main():
    user_input = input("문자열을 입력하세요: ")
    reversed_string = reverse_string(user_input)
    print("입력한 문자열의 역순:", reversed_string)

if __name__ == "__main__":
    main()

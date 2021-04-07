# 리스트를 활용한 스택 사용해보기
data_stack = list()

data_stack.append(1)
data_stack.append(2)

# 리스트 출력
print(data_stack)
# output : [1, 2]

# 리스트에서 데이터 꺼내기
print(data_stack.pop())
# output : 2

# pop, push 기능 구현
stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    # 마지막 데이터를 data에 설정한다.
    data = stack_list[-1]
    del stack_list[-1]
    return data

# 데이터 넣기
for index in range(10):
    push(index)

# 데이터 꺼내기
print(pop())
class Node:
    def __init__(self, data, next=None):   # self 인자값은 항상 앞쪽에 선언하지만, 사용하지는 않는다.
        self.data = data    # Node 객체가 생성될때 입력되는 데이터
        self.next = next    # 다음 Node를 가리키는 변수

def add(data):
    # 첫번째 node를 설정
    node = head
    # head node에서 마지막 노드를 찾아 node에 설정
    while node.next:    # node의 next가 있는지 확인
        node = node.next
    # 데이터를 Node로 생성하여 연결하기
    node.next = Node(data)

# Node 생성
node1 = Node(1)
node2 = Node(2)
# Node 연결하기
node1.next = node2

# 가장 앞의 노드를 선언
head = node1

# 링크드 리스트에 데이터 추가하기
# for문 1 ~ 9 (range : 1 <= i < 10)
# for i in range(1,10):
#     print(i)

# 3~9까지 add 함수를 통해 node를 추가하기
for index in range(3, 10):
    add(index)

# 데이터 출력하기
node = head
while node.next:
    print(node.data)
    node = node.next
# 마지막 노드 데이터 출력
print(node.data)


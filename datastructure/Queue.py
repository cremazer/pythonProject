# 큐 라이브러리를 import
import queue

# 일반적인 큐
data_queue = queue.Queue()
# 데이터 넣기
data_queue.put('Lucky')
data_queue.put('20210401')

# 등록된 데이터 개수 확인
size = data_queue.qsize()
print('size=', size)

# 큐에서 데이터 꺼내기(get)
print(data_queue.get())
# 등록된 데이터 개수 확인
print('size=', data_queue.qsize())
print(data_queue.get())


# Lifo 큐 (LIFO : Last-In, First-Out)
lifo_queue = queue.LifoQueue()
# 데이터 넣기
lifo_queue.put('Joy')
lifo_queue.put('20210401')

# 등록된 데이터 개수 확인
size = lifo_queue.qsize()
print('size=', size)

# 큐에서 데이터 꺼내기(get)
print(lifo_queue.get())
# 등록된 데이터 개수 확인
print('size=', lifo_queue.qsize())
print(lifo_queue.get())


# 우선순위 큐 (Priority Queue)
priority_queue = queue.PriorityQueue()

# 데이터 넣기 (우선순위, 데이터)
priority_queue.put((10, "Computer"))
priority_queue.put((5, "House"))
priority_queue.put((20, "Car"))

# 등록된 데이터 개수 확인
size = priority_queue.qsize()
print('size=', size)

# 큐에서 데이터 꺼내기(get)
print(priority_queue.get())


# 리스트를 활용하여 큐 기능 구현하기
queue_list = list()

# 데이터를 넣는 함수
def enqueue(data):
    queue_list.append(data)

# 데이터를 꺼내는 함수
def dequeue():
    data = queue_list[0]
    # 데이터를 꺼낸 후에 리스트에서 삭제해줘야 한다.
    del queue_list[0]
    return data

# 데이터 넣기 (0부터 9)
for index in range(10):
    enqueue(index)

# 등록된 리스트 개수 확인
print('list size=', len(queue_list))

# 큐에서 데이터 추출하기
print(dequeue())
print(dequeue())
print(dequeue())
# 1차원 배열 (리스트로 구현)
data1 = [1,2,3,4,5]
print(data1)

# 2차원 배열 (리스트로 구현)
data2 = [[1,2,3],[4,5,6],[7,8,9]]
print(data2)
print(data2[0])
print(data2[0][0])
print(data2[0][1])
print(data2[0][2])
print(data2[1][0])

# data2에서 9,8,7 순서로 출력
print(data2[2][2])
print(data2[2][1])
print(data2[2][0])
print(data2[2][2], data2[2][1], data2[2][0])

# dataset에서 문자 'M'이 포함된 문자열 개수 출력
dataset = [
'Vander',
'Miss. Ellen',
'Masselmani',
'Todoroff',
'Mr.William'
]

# 빈도수 변수 선언
m_count = 0
for str in dataset:
    #print(str)
    # 문자열 길이만큼 반복
    for index in range(len(str)):
        #print(str[index])
        if str[index] == 'M':
            #M이 있으면 빈도수 1씩 증가
            #m_count = m_count + 1 줄임표현식
            m_count += 1

print(m_count)

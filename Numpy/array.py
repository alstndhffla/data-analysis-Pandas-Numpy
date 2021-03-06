import numpy as np

"""
넘파이는 기본적으로 배열을 표현하기 위한 패키지이다.
np.array([]) -> 안에 리스트 형태로 집어넣음

"""

a = np.array([[2, 3], [5, 2]])
print(a)


print("-----------------------------------------")
# 배열 슬라이싱. 넘파이는 리스트보다 숫자를 다루는데 더 강력하고 특화되어있다.
d = np.array([[1,2,3,4,5], [2,4,5,6,7,], [5,7,8,9,9]])
# 3열 * 5행 배열
d = np.array([[1,2,3,4,5],
              [2,4,5,6,7,],
              [5,7,8,9,9]])

print(d)

print("-----------------------------------------")
# 배열 슬라이싱. 넘파이는 리스트보다 숫자를 다루는데 더 강력하고 특화되어있다.
print(d[1][2])
print(d[1, 2])  # 이와 같이 변형되어서도 사용. 인덱스 번호를 붙이는 것.

print(d[1:][3:])    # 이건 아무런 값도 출력하지 않음.
print(d[1:, 3:])    # 지정된 인덱스 뒤부터 다 출력 -> 새로운 배열이 된다.


print("-----------------------------------------")
# 배열의 크기를 알 수 있는 명령어 shape
print(d.shape)  # 행 * 열 로 표현해준다 (3, 5)


e = np.array([1, 2, 3, 4, 5])
print(e.shape)

f = np.array([[1, 2, 3, 4], [3, 4, 5, 6]])
print(f.shape)


print("-----------------------------------------")
# 배열의 원소 유형 확인하기 dtype
# 배열의 데이터가 숫자면 연산을 할 수 있고, 문자면 정규식을 사용할 수 있다.
print(d.dtype)


print("-----------------------------------------")
# 배열 유형바꾸기 astype()
data = np.arange(1, 5)
print(data.dtype)
print(data)
print(data.astype('float64'))

print("-----------------------------------------")
print(np.zeros((2, 10)))

print(np.ones((2, 10)))

# 2이상 10미만
print(np.arange(2, 10))

# 행과 열을 바꾸기(전치행렬)
# 2 * 3 행렬
a = np.ones((2, 3))
print(a)
# 3 * 2 행렬로 변환
b = np.transpose(a)
print(b)


print("-----------------------------------------")
# 크기가 서로 다른 배열끼리 더하기 (브로드캐스팅이라 한다 - 인공지능에 많이 쓰임) -> 행과 열의 크기가 모두 다르면 더할 수 없다.
# 둘 중 하나는 같아야 함.
# 각 행에 더해짐.
arr1 = np.array([[2, 3, 4], [6, 7, 8]])
arr3 = np.array([100, 200, 300])

print(arr1 + arr3)


print("-----------------------------------------")
# 배열과 리스트의 차이점은 리스트는 슬라이싱한 후 저장이 되지 않지만 배열은 슬라이싱 후 데이터를 저장할 수 있다.
arr4 = np.arange(10)
print(arr4)

print(arr4[:5])
print(arr4[-3:])

print("-----------------------------------------")
# 리스트가 여러개 있다면?
print(arr1)
print(arr1[:, 2])
print(arr1[1, 2])
print(arr1[1:, 2])


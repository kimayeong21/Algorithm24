#문제 20번 
def check_common_items(list1, list2):
    # 두 리스트 중 어느 하나라도 빈 리스트이면 False 반환
    if not list1 or not list2:
        return False

    # 한 리스트를 집합(set)으로 변환하여 중복된 항목을 빠르게 확인
    set1 = set(list1)

    # 두 번째 리스트를 순회하면서 중복된 항목이 있는지 확인
    for item in list2:
        if item in set1:
            return True

    # 중복된 항목이 없으면 False 반환
    return False

# 예시 리스트
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [5, 10, 15, 20]

# 두 리스트 간에 공통된 항목이 있는지 확인
print(check_common_items(list1, list2))  # False
print(check_common_items(list1, list3))  # True

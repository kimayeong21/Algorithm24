#단순연결리스트 구조를 이용해 이를 구현하라.
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link
def main():
    # 사용자로부터 노드의 개수 입력 받기
    num_nodes = int(input("노드의 개수: "))
    # 노드 데이터를 저장할 리스트 초기화
    nodes = []
    # 각 노드의 데이터 입력 받기
    for i in range(1, num_nodes + 1):
        data = int(input(f"노드 #{i} 데이터: "))
        node = Node(data, None)
        nodes.append(node)
    # 리스트의 내용 출력
    print("리스트의 내용:", [node.data for node in nodes])
if __name__ == "__main__":
    main()
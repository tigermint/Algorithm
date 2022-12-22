from queue import PriorityQueue


class HuffNode:
    # constructor
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    # method - 탐색
    def preorder(self):
        print(str(self.symbol) + ":" + str(self.freq), end=" ")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(str(self.symbol) + ":" + str(self.freq), end=" ")
        if self.right is not None:
            self.right.inorder()


def huffman(n, PQ):
    for _ in range(n - 1): # n - 1번 하는 이유: 1,2,3,4,5 라면 합하기 위해서는 연산 4번
        # PQ에 넣었을 경우 빈도를 기준으로 정렬된다.
        p = PQ.get()[1] # PQ의 첫번째 원소
        q = PQ.get()[1] # PQ의 두번째 원소
        r = HuffNode('+', p.freq + q.freq) # 합해서 새로운 노드 만들기, 딱히 문자가 필요 없기 때문에 "+"문자 삽입
        r.left = p  # 0, 자식 노드
        r.right = q  # 1, 자식 노드
        PQ.put((r.freq, r)) # r을 우선순위 큐에 넣음, 튜플 형식으로 넣는다
    return PQ.get()[1]

# inorder traversel로 이진 트리를 순회하면서 해당 문자당 인코딩 결과를 저장 -> 필요할 때마다 불러오면 된다.
def encoding(root, arr, dic):
    if root.left is not None:
        arr += '0'
        encoding(root.left, arr, dic)
    if root.symbol != '+':
        dic[root.symbol] = arr
    arr = arr[:-1]
    if root.right is not None:
        arr += '1'
        encoding(root.right, arr, dic)


def decoding(root, decodingList):
    node = root
    for i in decodingList:
        if i == 0: # 0일 경우 left로 이동
            node = node.left
        elif i == 1: # 1일 경우 right로 이동
            node = node.right
        if node.left == None and node.right == None: # leaf node일 경우 해당 문자열에 대한 디코딩이 끝났기 때문에 문자 출력 
            print(node.symbol, end="")
            node = root # 다시 root부터 출발해야 하기 때문에 root로 이동


# input
n = int(input())
code = list(input().split(" "))
freq = list(map(int, input().split(" ")))

# T1 = int(input())  # encoding
# encodingLists = [input() for _ in range(T1)]
T2 = int(input())  # decoding
decodingLists = [list(map(int, input())) for _ in range(T2)]


# Priority queue
PQ = PriorityQueue() # 정렬을 위한 우선순위 큐
for i in range(n):
    node = HuffNode(code[i], freq[i]) # 튜플 형식으로 우선 순위 큐에 삽입
    PQ.put((node.freq, node)) # node.freq, 즉 빈도수를 기준으로 PQ를 만든다. 

root = huffman(n, PQ)

dic = {}
for key in code:
    dic[key] = ""

# print -> 다른거 만들고 싶으면 위의 class method 추가하면 된다
# root.preorder()
# print()
root.inorder()
print()

# # encoding, decoding
# arr = ""
# encoding(root, arr, dic)

# for encodingList in encodingLists:
#     for i in encodingList: # 인코딩 리스트의 각 문자를 불러온다.
#         print(dic[i], end='')
#     print()

for decodingList in decodingLists: 
    decoding(root, decodingList) # 디코딩 문자열을 따라 0이면 왼쪽, 1이면 오른쪽으로 가서 만약 특정 문자가 나온다면 그게 leaf node이며 해당 디코딩 result
    print()
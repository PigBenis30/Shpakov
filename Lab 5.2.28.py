import random

class BinHeap:
    def __init__(self):
        self.heaplist = []
        self.heapsize = 0

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heapsize and self.heaplist[l] > self.heaplist[i]:
            largest = l
        else:
            largest = i
        if r <= self.heapsize and self.heaplist[r] > self.heaplist[largest]:
            largest = r
        if largest != i:
            tmp = self.heaplist[i]
            self.heaplist[i] = self.heaplist[largest]
            self.heaplist[largest] = tmp
            self.heapify(largest)

    def buildHeap(self, list):
        self.heaplist = list
        self.heapsize = len(list) - 1
        for i in range(len(list) // 2, -1, -1):
            self.heapify(i)
            
    def getHeap(self):
        return self.heaplist

def leaves(heap):
    leaves = []
    num_of_leaves = 0
    if len(heap) % 2 == 0:
        num_of_leaves = len(heap) / 2
    else:
        num_of_leaves = len(heap) // 2 + 1
    num_of_leaves = int(num_of_leaves)
    for i in range(num_of_leaves):
        leaves.append(heap[-1 - i])
    leaves.reverse()
    return leaves

def random_item():
    n = random.randint(1, 7)
    item = ""
    letters = "qwertyuiopasdfghjklzxcvbnm"
    for i in range(n):
        item += random.choice(letters)
    return item

def is_mult(deck):
    num = 0
    for char in deck:
        num += ord(char)
    if num % 2 == 0:
        return True
    else:
        return False

def input_num():
    x = ""
    print("Введите число количества узлов бинарной кучи (бинарного дерева): ")
    while True:
        x = input()
        try:
            x = int(x)
            return int(x)
        except ValueError:
            print("Неверное значение: ")

def main():
    heap = BinHeap()
    n = input_num()
    list = []
    for i in range(n):
        list.append(random_item())
    print("Входные данные: \n", list)
    heap.buildHeap(list)
    print("Структура данных, отсортированная по правилу полного (сбалансированного) бинарного дерева: \n", heap.getHeap())
    tree_leaves = leaves(heap.getHeap())
    steck = []
    print("Листья дерева: \n", tree_leaves)
    for i in range(len(tree_leaves)):
        if is_mult(tree_leaves[i]):
            steck.append(tree_leaves[i])
    print("Конечный ответ (листья с четной суммой кодов): \n", steck)

if __name__ == "__main__":
    main()

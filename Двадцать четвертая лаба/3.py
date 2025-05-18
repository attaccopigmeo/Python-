"""Ученые изучают поведение птиц, вьющих гнезда на бинарном дереве, и хотят
разместить в его узлах камеры. Каждая камера может обозревать узел, в котором она
расположена, а также непосредственного предка и непосредственных потомков этого узла. По
заданному бинарному дереву требуется определить, какое минимальное количество камер
потребуется ученым для того, чтобы полностью покрыть наблюдением все узлы дерева."""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


CAMERA = 0 # имеется камера
COVERED_BY_CHILD = 1 # узел покрыт потомком
NOT_COVERED = 2 # узел не покрыт (и нужно добавить камеру в родителя)


def find_solution(node):
    cameras = 0
    status = COVERED_BY_CHILD

    if node is not None: # пустые узлы считаем покрытыми потомками
        left_status, left_cameras = find_solution(node.left)
        right_status, right_cameras = find_solution(node.right)

        cameras = left_cameras + right_cameras

        # если хотя бы один из потомков не покрыт, нужно покрыть его камерой в текущем узле
        if left_status == NOT_COVERED or right_status == NOT_COVERED:
            cameras += 1
            status = CAMERA
        # если хотя бы в одном из потомков имеется камера, узел покрыт
        elif left_status == CAMERA or right_status == CAMERA:
            status = COVERED_BY_CHILD
        # иначе узел не покрыт
        else:
            status = NOT_COVERED
    
    return status, cameras


if __name__ == '__main__':
    with open('Двадцать третья лаба/1.txt', 'r') as f:
        nodes = [(Node(int(x)) if x != '0' else None) for x in f.readline().split()]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if 2 * i + 1 >= len(nodes):
            continue
        node.left = nodes[2 * i + 1]
        node.right = nodes[2 * i + 2]
    root = nodes[0]
    del nodes

    root_status, cameras = find_solution(root)
    if root_status == NOT_COVERED:
        cameras += 1 # нужно покрыть корень
    print('Требуемое количество камер:', cameras)
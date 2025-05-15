def move_node(relation, pre_node, network, cnt, pre_node_list):
    pre_node_list.append(pre_node + 1)
    if relation[pre_node]:
        for i, to_node in enumerate(relation[pre_node]):
            if to_node == pre_node:
                network[cnt].append(pre_node)
            elif to_node in pre_node_list:
                network[cnt].append(pre_node + 1)
                pass
            else:
                move_node(relation, to_node - 1, network, cnt, pre_node_list)
                network[cnt].append(to_node)
    else:
        network[cnt].append(pre_node + 1)


def solution(n, computers):
    answer = 0
    relation = []
    network = [[1]]
    node_row = 0
    node_column = 0
    cnt = 0
    pre_node_list = []
    for row in computers:
        relation.append([])
        for element_column in row:
            if node_row == node_column:
                pass
            elif element_column == 1:
                relation[node_row].append((node_column + 1))
            node_column = node_column + 1
        node_row = node_row + 1
        node_column = 0
    node_row = 0
    pre_node_list = []
    for idx in range(n):
        if idx + 1 in network[cnt]:
            pass
        else:
            network.append([])
            cnt = cnt + 1
            move_node(relation, idx, network, cnt, pre_node_list)
            pre_node_list = []
    # print(network)
    # print(relation)
    # print(len(network))
    # print(set(network))
    return len(network) - 1

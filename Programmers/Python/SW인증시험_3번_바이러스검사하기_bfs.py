def solution(folders, files, selected, excepted):
    answer = [0, 0]
    folders_path = {}
    files_path = {}

    for sfolder_, pfolder_ in folders:
        folders_path[pfolder_] = folders_path.get(pfolder_, []) + [sfolder_]

    for file_, size_, folder_ in files:
        if size_[-2] == "K":
            size_ = int(size_[:-2]) * 1024
        else:
            size_ = int(size_[:-1])
        files_path[folder_] = files_path.get(folder_, []) + [[file_, size_]]

    stack = [i for i in selected]
    selected_folders = set([])
    # print("folders_path :", folders_path)
    # print("files_path :", files_path)

    while stack:
        folder_ = stack.pop()
        selected_folders.add(folder_)

        while folder_ in folders_path and len(folders_path[folder_]) != 0:
            stack.append(folders_path[folder_].pop())

    for sf_ in selected_folders:
        if sf_ in files_path:
            for file_, size_ in files_path[sf_]:
                if file_ in excepted:
                    pass
                else:
                    answer[0] += size_
                    answer[1] += 1
    # print("selected_folders :", selected_folders)
    return answer


print(
    solution(
        [["animal", "root"], ["fruit", "root"]],
        [["cat", "1B", "animal"], ["dog", "2B", "animal"], ["apple", "4B", "fruit"]],
        ["animal"],
        ["apple"],
    )
    == [3, 2]
)
print(
    solution(
        [["food", "root"], ["meat", "food"], ["fruit", "food"], ["animal", "root"]],
        [
            ["cat", "1B", "animal"],
            ["dog", "2B", "animal"],
            ["fork", "1KB", "meat"],
            ["beef", "8KB", "meat"],
            ["apple", "4B", "fruit"],
            ["fire", "83B", "root"],
        ],
        ["root", "meat"],
        ["fork", "apple"],
    )
    == [8278, 4]
)

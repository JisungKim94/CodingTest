def solution(triangle):
    for idx_triangle, row in enumerate(triangle):
        for idx_row, element in enumerate(row):
            if idx_triangle == 0:
                pass
            else:
                # 제일 왼쪽은 싹다 왼쪽으로 더하기
                if idx_row == 0:
                    row[idx_row] = row[idx_row] + pre_row[idx_row]
                # 제일 오른쪽은 싹다 오른쪽으로 더하기
                elif idx_row == len(row) - 1:
                    row[idx_row] = row[idx_row] + pre_row[idx_row - 1]
                # 가운데 애들은 본인 위에 두 개 중에 큰 애를 더하기
                # 위에 두 개 를 사용하기 위해 pre_row 저장
                else:
                    row[idx_row] = row[idx_row] + max(
                        pre_row[idx_row], pre_row[idx_row - 1]
                    )
        pre_row = row
    return max(row)


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])

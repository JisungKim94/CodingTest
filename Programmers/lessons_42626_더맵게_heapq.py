############################################################################
import heapq

# heapq란 일반적인 리스트와 달리 이진트리 구조를 사용한 최소 힙 형태로 정렬
# 아래 주석 처리된 코드 실행 해보면 이해에 도움이 댐
# heap = []
# for i in scoville:
#     heapq.heappush(heap, i)
#     print(heap)
# for i in scoville:
#     print(heapq.heappop(heap))


# +alpha) 파이썬 heapq는 최소 힙으로 구성되어 있으므로 최대 힙을 만드려면
# 트릭이 필요하다. -1과 (-item, item) 튜플 형식의 트릭
#
# import heapq

# heap_items = [-1, -1, -3, 0, 0, 5, 5, 7, 9]
# max_heap = []
# for item in heap_items:
#     heapq.heappush(max_heap, (-item, item))
# print(max_heap)
# max_item = heapq.heappop(max_heap)[1]
# print(max_item)

# max_heap_2 = []
# for item in heap_items:
#     heapq.heappush(max_heap_2, -item)
# print(max_heap_2)
# max_item = -heapq.heappop(max_heap_2)
# print(max_item)
############################################################################

scoville = [1, 2, 3, 9, 10, 12]
# scoville = [1, 2, 3, 0, 0]
K = 7


def solution(scoville, K):
    answer = 0
    heap = []
    # heapq를 사용하면 속도가 쥰내 빠르군
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        # try except IndexError를 사용하는 센스
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        answer = answer + 1

    return answer


print(solution(scoville, K))

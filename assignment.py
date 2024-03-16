import heapq

def min_cost_to_connect_cables(cables):
    min_heap = cables[:]
    heapq.heapify(min_heap)
    total_cost = 0

    while len(min_heap) > 1:
        cable1 = heapq.heappop(min_heap)
        cable2 = heapq.heappop(min_heap)

        cost = cable1 + cable2
        total_cost += cost
        heapq.heappush(min_heap, cost)

    return total_cost



cables = [7, 3, 12, 5, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"Мінімальна вартість з'єднання кабелів: {min_cost}")

# Priority Queue using Binary Max-Heap
# MSCS 532 - Assignment 4

class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []  # list to store heap elements

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2

        while index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left].priority > self.heap[largest].priority:
                largest = left

            if right < size and self.heap[right].priority > self.heap[largest].priority:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

    def increase_key(self, task_id, new_priority):
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority > task.priority:
                    task.priority = new_priority
                    self._heapify_up(index)
                return

    def decrease_key(self, task_id, new_priority):
        for index, task in enumerate(self.heap):
            if task.task_id == task_id:
                if new_priority < task.priority:
                    task.priority = new_priority
                    self._heapify_down(index)
                return


if __name__ == "__main__":

    pq = PriorityQueue()

    # Insert tasks
    pq.insert(Task("T1", 5))
    pq.insert(Task("T2", 10))
    pq.insert(Task("T3", 3))
    pq.insert(Task("T4", 8))

    print("Heap after insertions:")
    print(pq.heap)

    # Extract max
    print("\nExtracted:", pq.extract_max())
    print("Heap after extraction:")
    print(pq.heap)

    # Increase priority
    pq.increase_key("T3", 12)
    print("\nHeap after increasing T3 priority to 12:")
    print(pq.heap)

    # Decrease priority
    pq.decrease_key("T3", 2)
    print("\nHeap after decreasing T3 priority to 2:")
    print(pq.heap)

# maxsize – Number of items allowed in the queue.
# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.
import queue

q = queue.Queue(maxsize=38)
for i in range(38):
  q.put(i + 1)

repeat = 0
while q.qsize() > 0:
  repeat += 1
  if repeat == 20:
    repeat = 0
    print(q.get())
    continue
  else:
    x = q.get()
    q.put(x)

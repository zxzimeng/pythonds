import timeit


class quicqueue:

  def __init__(self):
    self.items = []
    self.offset = 0

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    val = self.items[0 + self.offset]
    self.offset += 1
    return val

  def queue(self):
    return self.items[self.offset:]

  def size(self):
    return len(self.items) - self.offset


queue = quicqueue()
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(99)
queue.dequeue()
print(queue.queue())
print(queue.size())

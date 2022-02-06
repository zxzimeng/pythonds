class Queue:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    if self.items:
      return False
    return True

  def enqueue(self, item):
    self.items.append(item)

  def dequeue(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)

  def queue(self):
    return self.items


a = Queue()
a.enqueue(0)
a.enqueue(9)
a.dequeue()
print(a.queue())
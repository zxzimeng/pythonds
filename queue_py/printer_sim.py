# empty() – Return True if the queue is empty, False otherwise.
# full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
# get() – Remove and return an item from the queue. If queue is empty, wait until an item is available.
# get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
# put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
# put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
# qsize() – Return the number of items in the queue.

from queue import Queue
import random

g_nextTaskId = 0


class Task:

  def __init__(self, time):
    global g_nextTaskId
    self.id = g_nextTaskId
    g_nextTaskId += 1
    self.timestamp = time
    self.pages = random.randrange(1, 21)

  def getStamp(self):
    return self.timestamp

  def getPages(self):
    return self.pages

  def waitTime(self, currenttime):
    return currenttime - self.timestamp

  def __str__(self) -> str:
    return f"id: {self.id} creation_time: {self.timestamp} pages: {self.pages}"


class Printer:

  def __init__(self, ppm):
    self.pagerate = ppm
    self.currentTask = None
    self.timeRemaining = 0
    self.queue = Queue()
    self.waitingTimes = []

  def tick(self, ticks):
    if self.currentTask is not None:
      self.timeRemaining = self.timeRemaining - 1
      if self.timeRemaining <= 0:
        self.currentTask = None
    if self.currentTask is None and not self.queue.empty():
      self.currentTask = self.queue.get()
      self.timeRemaining = self.currentTask.getPages() * 60 / self.pagerate

      # print(
      #     f"printing: {self.currentTask.id} wait time:{self.currentTask.waitTime(ticks)}"
      # )
      self.waitingTimes.append(self.currentTask.waitTime(ticks))

  def busy(self):
    if self.currentTask != None:
      return True
    else:
      return False

  def addTask(self, task: Task):
    self.queue.put(task)

  def getWaitingTimes(self):
    return self.waitingTimes


def maybeGenerateTask(ticks: int) -> Task:
  if random.randint(0, 180) == 180:
    return Task(ticks)
  return None


def sim(duration: int, ppm: int):
  ticks = 0
  printer = Printer(ppm)
  while ticks < duration:
    task = maybeGenerateTask(ticks)
    if task is not None:
      printer.addTask(task)
    printer.tick(ticks)
    ticks += 1
  while printer.busy():
    printer.tick(ticks)
    ticks += 1
  return printer.waitingTimes


def avgSim(ppm):
  avgL = []

  for i in range(1000):
    waitList = sim(3600, ppm)
    avgL.append(int(sum(waitList) / len(waitList)))
  return int(sum(avgL) / len(avgL))


for i in range(1, 10):
  print(i, avgSim(i))

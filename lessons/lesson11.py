#stack
stack = []
def push(value):
    stack.append(value)

def pop():
    return stack.pop()

def peek():
    return stack[len(stack)-1]

def isEmpty():
    return stack == []

#push(1)
#push(5)
#push(11)
#push(4)
#print(stack)
#print(pop())
#print(stack)
#print(isEmpty())

#queue
queue = []

def push_q(value):
    queue.append(value)

def pop_q():
    return queue.pop(0)

def peek_q():
    return queue[0]

def isEmpty_q():
    return queue == []

push_q(1)
push_q(5)
push_q(11)
push_q(4)
print(queue)
print(pop_q())
print(queue)
print(isEmpty_q())

from queue import LifoQueue, Queue

stack_1 = LifoQueue()
stack_1.put(1)
stack_1.put(2)
stack_1.put(3)
stack_1.get()
print(stack_1.queue)

queue_1 = Queue()
queue_1.put(1)
queue_1.put(2)
queue_1.put(3)
queue_1.get()
print(queue_1.queue)

#graphs
from networkx import Graph

graph = Graph()

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)

graph.add_edge(1, 2)
graph.add_edge(1, 3)

print(graph.adj)
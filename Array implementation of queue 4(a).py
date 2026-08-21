queue = [None] * 5
front = -1
rear = -1
def enqueue(x):
    global front, rear
    if rear == 4:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = x
        print("Inserted:", x)
def dequeue():
    global front, rear
    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print("Deleted:", queue[front])
        front += 1
def display():
    if front == -1 or front > rear:
        print("Queue is Empty")
    else:
        print("Queue:",queue[front:rear+1])
choice=int(input("Enter a choice:"))
if choice==1:
    n=int(input("Enter number of times to insert"))
    for i in range(n):
        a=int(input("Enter element to insert:"))
        enqueue(a)
    display()
elif choice==2:
    print("Dequeue")
    dequeue()
    display()
else:
    print("Invalid")

import queue
import threading
import turtle

def tes1():
    for _ in range(360):
        for i in range(10):
            graphics.put(turtle1.forward)
            graphics.put(turtle1.left)
            #graphics.put(turtle1.forward(100))  ## <- error !! because of real parameter... (100)
            #graphics.put(turtle1.left(90))
            #graphics.put(turtle1.forward(100))
            #graphics.put(turtle1.left(90))

def tes2():
    for _ in range(360):
        for i in range(10):
            graphics.put(turtle2.forward)
            graphics.put(turtle2.right)

def process_queue():
    while not graphics.empty():
        (graphics.get())(1)

    if threading.active_count() > 1:
        turtle.ontimer(process_queue, 100)

graphics = queue.Queue(1)  # size = number of hardware threads you have - 1

turtle1 = turtle.Turtle('turtle')
turtle1.pensize(5)
turtle1.color("red")
thread1 = threading.Thread(target=tes1)
thread1.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread1.start()

turtle2 = turtle.Turtle('turtle')
turtle2.pensize(5)
turtle2.color("blue")
thread2 = threading.Thread(target=tes2)
thread2.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
thread2.start()

process_queue()




input("")
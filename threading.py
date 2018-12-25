import threading 
import datetime
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(11,)) 
    t2 = threading.Thread(target=print_cube, args=(3,)) 
    print(datetime.datetime.now())
    # starting thread 1 
    t1.start() 
    print(datetime.datetime.now())
    # starting thread 2 
    t2.start() 
    print(datetime.datetime.now())
    # wait until thread 1 is completely executed 
    t1.join() 
    print(datetime.datetime.now())
    # wait until thread 2 is completely executed 
    t2.join() 
    print(datetime.datetime.now())
  
    # both threads completely executed 
    print("Done!")
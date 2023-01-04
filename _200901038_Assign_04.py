import threading
import time

user_string = ''

class MainThread:
  def __init__(self, string):
    self.string = string

  def input_thread(self):
    user_string = input(str("Enter a string: "))
    return user_string

  def reverse_thread(self, string):
    return string[::-1] 

  def capital_thread(self, string):
    return string.upper()

  def shift_thread(self, string):
    array = list(string)
    size = len(array)
    new_array = []

    for i in range (0, size):
      code = chr(ord(array[i]) + 2)
      new_array.append(code)

    ' '.join(new_array)


mt = MainThread(user_string)

t1 = threading.Thread(target = mt.input_thread)       
t2 = threading.Thread(target = mt.reverse_thread, args = (user_string))    
t3 = threading.Thread(target = mt.capital_thread, args = (user_string))  
t4 = threading.Thread(target = mt.shift_thread, args = (user_string))

t1.start()                                        
time.sleep(1.0)                                  
t1.join()

t2.start()                                                                                
t3.start()
t2.join()
t4.start()
t3.join()
t4.join()



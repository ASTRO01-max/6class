# class Stack:
#     def __init__(self):
#         self.lst = []
        
#     def stack(self):
#         for i in self.lst:
            # if i == "(":
            #     i+=1
            # elif i == ")":
            #     i-=1
            # if i == 0:
            #     return  self.lst.pop() 

    # def push(self, item):
    #     self.lst.append(item)

    # def pop(self):
    #     if not self.empty():
    #         return self.lst.pop()
    #     return None  

#     def empty(self):
#         if not self.lst:
#             return True


class Stack:
    def __init__(self):
        self.lst = []
    
    def add(self, item):
        self.lst.append(item)

    def empty(self):
        if not self.lst:
            return True

    def pop(self):
        if not self.empty():
            return self.lst.pop()
        return None  
    

def stack(qavus):
    stack = Stack()
    for i in qavus:
        if i == "(":
            stack.add(i) 
        elif i == ")":
            if stack.empty():
                return False 
            stack.pop()  

    return stack.empty()


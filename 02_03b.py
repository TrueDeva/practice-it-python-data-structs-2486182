from collections import deque

class taskMaster:
    def __init__(self, taskdq):
        self.taskdq = deque(maxlen=10)


    def addTask(self, task, priorityflag):
        if priorityflag == True:
            self.taskdq.append((task, priorityflag))
        else:
            self.taskdq.appendleft((task, priorityflag))    

    def getTask(self):
        if len(self.taskdq) > 0:
            return self.taskdq.pop()
        else:
            return 0
    
    def getAlltsk(self):
        if len(self.taskdq) > 0: 
            return list(self.taskdq)
        else:
            return "EMPTY"

 
def main():
    proddq = deque(maxlen=10)
    prodtask = taskMaster(proddq)
    prodtask.addTask("Prepare for wedding next week", False)
    prodtask.addTask("Find leads", False)
    prodtask.addTask("Buy supplies", True)
    prodtask.addTask("Hire new personnel", False)
    prodtask.addTask("Do taxes", True)
    #print(prodtask.getAlltsk())
    while prodtask.getAlltsk() != "EMPTY":
        print(prodtask.getTask())
        print(prodtask.getAlltsk())
 
    return

if __name__ == "__main__":
    main()
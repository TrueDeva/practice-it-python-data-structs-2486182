from collections import deque

class TaskMaster(object):
    def __init__(self, taskdq=None):
        self.taskdq = taskdq if taskdq is not None else deque(maxlen=10)

    def __str__(self):
        if not self.taskdq:
            return "Taskmaster: Nothin in queue"
        tasks_str = ", ".join(["Task: {0}, Priority: {1}".format(task[0], task[1]) for task in self.taskdq])
        return f"TaskMaster with tasks: [{tasks_str}]"

    def add_task(self, taskid, task_flag=False):
        if task_flag:
            self.taskdq.appendleft((taskid, task_flag))
        else:
            self.taskdq.append((taskid, task_flag))

    def get_task(self):
        if self.taskdq:
            return self.taskdq.pop()
        return None
                            
    def get_all_tasks(self):
        if self.taskdq:
            return list(self.taskdq)
        return "EMPTY"    
        

 
def main():
    prodtask = TaskMaster()
    prodtask.add_task("Prepare for wedding next week", False)
    prodtask.add_task("Find leads", False)
    prodtask.add_task("Buy supplies", True)
    prodtask.add_task("Hire new personnel", False)
    prodtask.add_task("Do taxes", True)
    #print(prodtask.get_all_tasks()) 
    print(prodtask)
    while True:
        task = prodtask.get_task()
        if task is None:
            break
        print(task)
    
    return

if __name__ == "__main__":
    main()
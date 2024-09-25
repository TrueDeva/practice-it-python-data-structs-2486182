from collections import deque

class TaskMaster:
    def __init__(self, taskdq=None):
        # Initialize with an empty deque if no deque is provided
        self.taskdq = taskdq if taskdq is not None else deque(maxlen=10)

    def add_task(self, task, priority_flag=False):
        # Add tasks based on priority
        if priority_flag:
            self.taskdq.appendleft((task, priority_flag))
        else:
            self.taskdq.append((task, priority_flag))

    def get_task(self):
        if self.taskdq:
            return self.taskdq.pop()
        return None
    
    def get_all_tasks(self):
        if self.taskdq:
            return list(self.taskdq)
        return "EMPTY"
 
def main():
    # Initialize TaskMaster without providing an external deque
    prodtask = TaskMaster()
    prodtask.add_task("Prepare for wedding next week")
    prodtask.add_task("Find leads")
    prodtask.add_task("Buy supplies", True)
    prodtask.add_task("Hire new personnel")
    prodtask.add_task("Do taxes", True)

    while True:
        task = prodtask.get_task()
        if task is None:
            break
        print(task)
        print(prodtask.get_all_tasks())
 
if __name__ == "__main__":
    main()

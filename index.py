from models.taskReader import TaskReader

inputPath = 'input/input.txt'

taskInput = TaskReader(inputPath)

print(taskInput.requests)
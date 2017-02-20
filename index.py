from models.taskReader import TaskReader

inputPath = 'input/small.in'

taskInput = TaskReader(inputPath)

matrix = taskInput.get_matrix()

print(matrix)

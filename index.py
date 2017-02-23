from models.taskReader import TaskReader

inputPath = 'input/input.txt'

taskInput = TaskReader(inputPath)

# print(taskInput.requests)

videos_size = taskInput.video_size

video_to_cache = [
    [0.95, 0.18, 0.52],
    [0.95, 0.18, 0.52],
    [0.95, 0.18, 0.52],
    [0.95, 0.18, 0.52],
    [0.95, 0.18, 0.52]
]
caches_free_space = [taskInput.cash_size for k in range(0, taskInput.n_caches)]

output = 'output/output.txt'
f = open(output, 'w')
f.write(str(taskInput.n_caches) + '\n')
for k in range(0, 1000):
    file_was_written = False
    for video_index in range(0, len(video_to_cache)):
        max_value_element = max(video_to_cache[video_index])
        cache_index = video_to_cache[video_index].index(max_value_element)

        cache_space = caches_free_space[cache_index]
        video_size = videos_size[video_index]
        if(cache_space > video_size):
            file_was_written = True
            caches_free_space[cache_index] = cache_space - video_size
            video_to_cache[video_index][cache_index] = 0
            f.write(str(cache_index) + ' ' + str(video_index) + ' ')

    if(file_was_written):
        f.write('\n')







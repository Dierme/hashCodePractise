class TaskReader(object):

    def __init__(self, filepath):

        self.__file = open(filepath, 'r')

        self.n_videos = 1
        self.n_endpoints = 1
        self.n_req_desc = 1
        self.n_caches = 1
        self.cash_size = 1

        self.__parse_first_line()

        self.video_size = self.__parse_video_size()

        self.datacenter = [0 for k in range(0, self.n_endpoints)]

        self.latency = self.__parse_endpoints()

        self.requests = self.__parse_requests()

    def __parse_first_line(self):

        first_line = self.__file.readline().strip().split(' ')

        self.n_videos = int(first_line[0])
        self.n_endpoints = int(first_line[1])
        self.n_req_desc = int(first_line[2])
        self.n_caches = int(first_line[3])
        self.cash_size = int(first_line[4])

        return True

    def __parse_video_size(self):
        second_line = self.__file.readline().strip().split(' ')
        video_size = [k for k in range(0, self.n_videos)]
        for i, value in enumerate(second_line):
            video_size[i] = int(value)

        return video_size

    def __parse_endpoints(self):
        latency = [k for k in range (0,self.n_endpoints)]

        for x in range(0, self.n_endpoints):
            endpoint_settings_line = self.__file.readline().strip().split(' ')
            self.datacenter[x] = int(endpoint_settings_line[0])
            n_caches = int(endpoint_settings_line[1])
            latency[x] = [0 for k in range(0, self.n_caches)]
            for y in range(0, n_caches):
                endpoint_x_setting = self.__file.readline().strip().split(' ')
                index = int(endpoint_x_setting[0])      #cache number
                value = int(endpoint_x_setting[1])      #latency
                latency[x][index] = value

        return latency

    def __parse_requests(self):
        requests = [[0 for k in range(0, self.n_videos)] for y in range(self.n_endpoints)]

        for x in range(0, self.n_req_desc):
            request_settings = self.__file.readline().strip().split(' ')

            video_number = int(request_settings[0])         # video number
            endpoint_number = int(request_settings[1])      # endpoint number
            request_value = int(request_settings[2])        # request
            requests[endpoint_number][video_number] = request_value

        return requests


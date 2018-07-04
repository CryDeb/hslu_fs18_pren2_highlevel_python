import threading


class LogList():

    # instance
    __instance = None

    log_list = []
    lock_log_list = threading.Lock()

    @staticmethod
    def get_instance():
        if LogList.__instance == None:
            LogList()
        return LogList.__instance

    def __init__(self):
        if LogList.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            LogList.__instance = self

    def add_log(self, log):
        self.lock_log_list.acquire()
        try:
            self.log_list.append(log)
        finally:
            self.lock_log_list.release()

    def clear_logs(self):
        self.lock_log_list.acquire()
        try:
            self.log_list.clear()
        finally:
            self.lock_log_list.release()

    def print_list(self):
        print(self.log_list)

    def get_log(self, index):
        self.lock_log_list.acquire()
        try:
            if len(self.log_list) > index:
                return self.log_list[index]
            else:
                return None
        finally:
            self.lock_log_list.release()

    def get_logs(self, index):
        self.lock_log_list.acquire()
        try:
            if len(self.log_list) > index:
                return self.log_list[index:]
            else:
                return None
        finally:
            self.lock_log_list.release()

    def get_size(self):
        self.lock_log_list.acquire()
        try:
            return len(self.log_list)
        finally:
            self.lock_log_list.release()

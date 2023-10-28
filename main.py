from numpy import random, arange
import simpy
import operator
import matplotlib.pyplot as plt


class Scheduler(object):
    def __init__(self, env, task_count, y_mean, x_rate, z_mean, k, quantum1, quantum2, duration):
        self.count = task_count
        self.y_mean = y_mean
        self.x_rate = x_rate
        self.z_mean = z_mean
        self.k = k
        self.quantum1 = quantum1
        self.quantum2 = quantum2
        self.env = env
        self.priority_queue = []
        self.round_robin_t1 = []
        self.round_robin_t2 = []
        self.first_come_first_serve = []
        self.priority_queue_count = []
        self.round_robin_t1_count = []
        self.round_robin_t2_count = []
        self.cpu_work_count = []
        self.waiting_time = []
        self.expired_processes = 0
        self.first_come_first_serve_count = []
        self.action = env.process(self.run())
        self.idle_status = True
        self.duration = duration

    def job_creator(self):
        pass

    def run(self):
        pass

    def check_timeout(self):
        pass

    def dispatcher(self):
        pass

    def job_loader(self):
        pass

    def __update_service_time_in_tuple(self, main_tuple, service_time):
        new_tuple = list(main_tuple)
        new_tuple[1] = service_time
        return tuple(new_tuple)

    def round_robin_t1_process(self, quantum_time):
        if len(self.round_robin_t1) == 0:
            self.round_robin_t1_count.extend([0] * (self.env.now - len(self.round_robin_t1_count)))
            self.idle_status = True
        for task in self.round_robin_t1:
            if task[1] <= quantum_time:
                self.round_robin_t1_count.extend(
                    [len(self.round_robin_t1)] * (self.env.now - len(self.round_robin_t1_count) - 1))
                self.waiting_time.append((self.env.now + task[1]) - task[0])
                self.round_robin_t1.remove(task)
                self.round_robin_t1_count.append(len(self.round_robin_t1))
                self.idle_status = False
                yield self.env.timeout(task[1])
            else:
                self.round_robin_t1_count.extend(
                    [len(self.round_robin_t1)] * (self.env.now - len(self.round_robin_t1_count) - 1))
                self.round_robin_t2.append(self.__update_service_time_in_tuple(task, task[1] - quantum_time))
                self.round_robin_t1.remove(task)
                self.round_robin_t1_count.append(len(self.round_robin_t1))
                self.idle_status = False
                yield self.env.timeout(quantum_time)

    def round_robin_t2_process(self, quantum_time):
        if len(self.round_robin_t2) == 0:
            self.round_robin_t2_count.extend([0] * (self.env.now - len(self.round_robin_t2_count)))
            self.idle_status = True
        for task in self.round_robin_t2:
            if task[1] <= quantum_time:
                self.round_robin_t2_count.extend(
                    [len(self.round_robin_t2)] * (self.env.now - len(self.round_robin_t2_count) - 1))
                self.waiting_time.append((self.env.now + task[1]) - task[0])
                self.round_robin_t2.remove(task)
                self.round_robin_t2_count.append(len(self.round_robin_t2))
                self.idle_status = False
                yield self.env.timeout(task[1])
            else:
                self.round_robin_t2_count.extend(
                    [len(self.round_robin_t2)] * (self.env.now - len(self.round_robin_t2_count) - 1))
                self.first_come_first_serve.append(self.__update_service_time_in_tuple(task, task[1] - quantum_time))
                self.round_robin_t2.remove(task)
                self.round_robin_t2_count.append(len(self.round_robin_t2))
                self.idle_status = False
                yield self.env.timeout(quantum_time)
    def first_come_first_serve_process(self):
        pass

    def analyse(self):
        pass

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

    def round_robin_t2_process(self):
        pass

    def first_come_first_serve_process(self):
        pass

    def analyse(self):
        pass

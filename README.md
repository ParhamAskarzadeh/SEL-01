# SEL-01

# cpu_scheduler_simulator

This is a Python code for a scheduler implementation that simulates different scheduling algorithms such as Priority Queue, Round Robin, and First Come First Serve. The scheduler schedules tasks based on their arrival time, service time, and priority. The code uses the SimPy library for discrete-event simulation.

## Installation

To run the code, you need to have Python installed on your system. Additionally, you need to install the following libraries:

- numpy
- simpy
- matplotlib

You can install these libraries using pip:

```
pip install numpy simpy matplotlib
```

## Usage

```python
python main.py
```

The code will simulate the scheduling of tasks using different algorithms and display the results.

## Description

The code defines a class `Scheduler` that represents the scheduler. The constructor of the `Scheduler` class takes several parameters:

- `env`: The SimPy environment object.
- `task_count`: The total number of tasks to be scheduled.
- `y_mean`: The mean value for the service time distribution.
- `x_rate`: The rate parameter for the arrival time distribution.
- `z_mean`: The mean value for the timeout distribution.
- `k`: The number of tasks to be loaded into the round-robin queues at each period.
- `quantum1`: The time quantum for the first round-robin queue.
- `quantum2`: The time quantum for the second round-robin queue.
- `duration`: The total simulation duration.

The `Scheduler` class has several methods:

- `job_creator`: Generates a new task with random arrival time, service time, priority, and timeout.
- `run`: The main simulation loop that runs until the specified duration. It creates the initial tasks, checks for timeout tasks, and dispatches tasks to different queues.
- `check_timeout`: Checks if any task has timed out and removes it from the corresponding queue.
- `dispatcher`: Randomly selects a scheduling algorithm (priority queue, round robin T1, or round robin T2) and dispatches the process.
- `job_loader`: Loads tasks from the priority queue into the round-robin queues based on the specified number `k`.
- `__update_service_time_in_tuple`: Helper method to update the service time in a task tuple.
- `round_robin_t1_process`: Implements the round-robin T1 scheduling algorithm.
- `round_robin_t2_process`: Implements the round-robin T2 scheduling algorithm.
- `first_come_first_serve_process`: Implements the first-come-first-serve scheduling algorithm.
- `__sort_priority_queue`: Sorts the priority queue based on priority and service time.
- `analyse`: Analyzes and displays the results of the simulation, including queue counts, mean delay, expired processes percentage, waiting time mean, and CPU worked time.


<div style="text-align: right;">

## پوشه‌ی .git
پوشه‌ی .git در یک مخزن Git شامل تمام اطلاعات مربوط به تاریخچه‌ی پروژه و تنظیمات Git می‌باشد. اطلاعات مهمی که در این پوشه ذخیره می‌شوند شامل موارد زیر می‌شوند:


1. شی‌ها (Objects): اشیاءی که در گیت ذخیره می‌شوند، مانند commit‌ها، tree‌ها و blob‌ها.

2. مراجعه‌گرها (References): فایل‌هایی که به شاخه‌های مختلف و commit‌ها اشاره دارند، مانند HEAD، شاخه‌ها (branches) و تگ‌ها (tags).

3. تنظیمات (Configurations): تنظیمات مربوط به پروژه و مخزن مانند نام و ایمیل نویسنده و تنظیمات مخزن.

4. فایل‌های‌ی .gitignore: فایل‌هایی که مشخص می‌کنند کدام فایل‌ها و دایرکتوری‌ها باید در تاریخچه Git ردیابی نشوند.

5. لاگ‌ها و فایل‌های خروجی: فایل‌هایی که مربوط به لاگ‌ها و خروجی‌های اجرای دستورات مختلف هستند.

پوشه‌ی .git به طور خودکار توسط Git ایجاد می‌شود و شما نیازی به ایجاد آن ندارید. برای شروع یک مخزن جدید، می‌توانید دستور `git init` را اجرا کنید.

## Atomic Commit و Atomic Pull Request
در مفهوم Atomic Commit، یک Commit باید یک واحد کاری را انجام دهد و تغییرات مرتبط با یک مسئله خاص را در خود داشته باشد. Atomic Commit به دیگر اعضای تیم کمک می‌کند تا تغییرات را برای مرور و بررسی آسان‌تری ارسال کنند.

Atomic Pull Request نیز به معنای ارسال یک Pull Request که شامل تغییرات یکسان و مرتبط با یک وظیفه یا مسئله خاص باشد است. این کار به تیم‌ها و مراجعین کمک می‌کند تا ارزیابی و ادغام تغییرات را ساده‌تر و اثربخش‌تر انجام دهند.

## تفاوت دستورهای Fetch، Pull، Merge، Rebase، Cherry-pick
1. `git fetch`: این دستور تغییرات از مخازن از راه دور (remote repositories) را به مخزن محلی شما دریافت می‌کند، اما تغییرات را به شاخه‌ی فعلی اعمال نمی‌کند.

2. `git pull`: این دستور تغییرات از مخازن از راه دور را دریافت کرده و آن‌ها را به شاخه‌ی فعلی اعمال می‌کند. ابتدا یک `git fetch` انجام می‌دهد و سپس با `git merge` یا `git rebase` تغییرات را اعمال می‌کند.

3. `git merge`: این دستور برای ادغام (merge) تغییرات از یک شاخه (branch) به شاخه‌ی فعلی استفاده می‌شود.

4. `git rebase`: این دستور تغییرات را از یک شاخه به شاخه فعلی انتقال می‌دهد و تاریخچه‌ی commit را مرتب‌تر می‌کند.

5. `git cherry-pick`: این دستور از یک commit خاص در یک شاخه دیگر تغییرات را به شاخه فعلی انتقال می‌دهد.

## تفاوت دستورهای Reset، Revert، Restore
1. `git reset`: این دستور برای بازگشت به commit خاصی در تاریخچه‌ی یک شاخه به‌کار می‌رود. این عمل باعث حذف commit‌های بعدی و تغییر تاریخچه می‌شود.

2. `git revert`: با این دستور یک commit خاص را با ایجاد یک commit دیگر که تغییرات معکوس شده‌ای از commit انتخابی را اعمال می‌کند، لغو می‌کند.

3. `git restore`: این دستور برای لغو تغییرات در فایل‌های کاری (working directory) به حالت commit انتخ

ابی بازمی‌گرداند.

## Stage
Stage به معنای آماده‌سازی تغییرات برای commit است. قبل از commit، تغییراتی که در working directory انجام داده‌اید، باید به stage (یا index) اضافه شوند. این کار با دستور `git add` انجام می‌شود.

## دستور stash
دستور `git stash` برای ذخیره تغییرات غیر commit شده در working directory مورد استفاده قرار می‌گیرد. این دستور تغییرات را در یک پشته (stash) موقت ذخیره می‌کند تا شما بتوانید به شاخه‌ی فعلی برگردید و سپس تغییرات را بازگردانی کنید.

## مفهوم Snapshot
در Git، هر commit یک snapshot از وضعیت فایل‌ها در زمان commit مربوطه را نشان می‌دهد. Snapshot به معنای یک تصویر از وضعیت فایل‌ها در زمان commit است. هر commit شامل تغییراتی است که به این snapshot اضافه شده‌اند و تاریخچه‌ی تغییرات شما را تشکیل می‌دهد. Snapshot به صورت immutable (غیرقابل تغییر) در Git نگهداری می‌شود و برای مقایسه و بازیابی تغییرات استفاده می‌شود.
</div>

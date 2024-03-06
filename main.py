"""
Venturenix Python coding contest 2024
main.py: the runner
*** DO NOT CHANGE ANYTHING IN THIS FILE ***
"""
import psutil
from pyinstrument import Profiler
from module import answer1, answer2, answer3
import gc
import time

num_of_runs: int = 7
valid_runs: list[int] = [1,2,3,4,5]

memory_usage: dict[float] = dict()
durations: dict[float] = dict()
cpu_time: dict[float] = dict()

print("Running answers...")
gc.collect()
profiler = Profiler()
for i in range(num_of_runs):
    profiler.start()
    # Participant code starts
    a = answer1(4)
    b = answer2(4)
    c = answer3(4)
    # Participant code ends
    profiler.stop()
    memory_usage[i] = psutil.Process().memory_info().rss / (1024*1024)
    durations[i] = profiler.last_session.duration
    cpu_time[i] = profiler.last_session.cpu_time
    profiler.reset()
    del(a, b, c)
    gc.collect()
memory_usage_avg = round(sum([memory_usage[i] for i in valid_runs])/len(valid_runs),5)
cpu_time_avg = round(sum([cpu_time[i] for i in valid_runs])/len(valid_runs),5)

# Using Pi as benchmark function
def cpu_benchmarking() -> None:
  start_benchmark: int = 3000 # samples
  repeat_benchmark: int = 5 # attemps
  average_benchmark: float = 0

  for a in range(0,repeat_benchmark):
    start = time.perf_counter()
    for i in range(0,start_benchmark):
      for x in range(1,1000):
        3.141592 * 2**x
      for x in range(1,10000):
        float(x) / 3.141592
      for x in range(1,10000):
        float(3.141592) / x

    end = time.perf_counter()
    duration = (end - start)
    duration = round(duration, 3)
    average_benchmark += duration

  average_benchmark = round(average_benchmark / repeat_benchmark, 5)
  return(average_benchmark)

print("Benchmarking...")
cpu_benchmark = cpu_benchmarking()
final_score = round(memory_usage_avg*1024 * (cpu_time_avg / cpu_benchmark),5)
print("\nReference\n---------")
print(f"Memory usage: {memory_usage_avg}Mb\nAverage CPU: {cpu_time_avg}\nBenchmark CPU time: {cpu_benchmark}")
print(f"Final Score (reference only): {final_score}")
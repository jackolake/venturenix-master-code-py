"""
Venturenix Python coding contest 2024
main.py: the runner
*** DO NOT CHANGE ANYTHING IN THIS FILE ***
"""
import psutil
import platform
from resource import getrusage, RUSAGE_SELF
from pyinstrument import Profiler
from module import answer1, answer2, answer3
import gc
import time

num_of_runs: int = 7
valid_runs: list[int] = [1,2,3,4,5]

memory_usage: dict[float] = dict()
durations: dict[float] = dict()
cpu_time: dict[float] = dict()

seed: int = 888888
answer1_assert: float = 17178313184.68749

def peak_mem():
  if platform.system() == 'Linux':
    return(getrusage(RUSAGE_SELF).ru_maxrss/1024)
  elif platform.system() == 'Windows':
    return(psutil.Process().memory_info().peak_wset / (1024*1024))
  elif platform.system() == 'Darwin':
    return(getrusage(RUSAGE_SELF).ru_maxrss/(1024*1024))

print("Running answers...")
gc.collect()
profiler = Profiler()
for i in range(num_of_runs):
    profiler.start()
    # Participant code starts
    assert answer1(seed)==answer1_assert, "function answer1 is incorrect"
    b = answer2(4)
    c = answer3(4)
    # Participant code ends
    profiler.stop()
    memory_usage[i] = peak_mem()
    durations[i] = profiler.last_session.duration
    cpu_time[i] = profiler.last_session.cpu_time
    profiler.reset()
    del(b, c)
    gc.collect()
memory_usage_avg = round(sum([memory_usage[i] for i in valid_runs])/len(valid_runs),5)
durations_avg = round(sum([durations[i] for i in valid_runs])/len(valid_runs),5)

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
final_score = round(memory_usage_avg*1024 * (durations_avg / cpu_benchmark),5)
print("\nReference\n---------")
print(f"Memory usage: {memory_usage_avg} Mb\nAverage runtime: {durations_avg}\nBenchmark CPU time: {cpu_benchmark}")
print(f"Final Score (reference only): {final_score}")
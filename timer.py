import time

class Timer:
	def __init__(self):
		self._start_time = None

	def start(self):
		self._start_time = time.perf_counter()

	def getTime(self):
		elapsed_time = time.perf_counter() - self._start_time
		return elapsed_time

	def stop(self):
		elapsed_time = time.perf_counter() - self._start_time
		self._start_time = None
		print(f"Elapsed time: {elapsed_time:0.9f} seconds")
	
	def maxTime(self):
		self._start_time = None
		print(f"No Solution!")
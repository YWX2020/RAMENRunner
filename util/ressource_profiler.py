import psutil
import time
import os
from functools import wraps

def measure_performance():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Initialize process info
            process = psutil.Process(os.getpid())
            start_cpu_time = process.cpu_times().user
            start_memory = process.memory_info().rss  # in bytes
            start_time = time.time()

            # Run the function
            result = func(*args, **kwargs)

            # Calculate performance metrics
            end_time = time.time()
            elapsed_time = end_time - start_time
            end_cpu_time = process.cpu_times().user
            cpu_time_used = end_cpu_time - start_cpu_time
            end_memory = process.memory_info().rss
            memory_used = (end_memory - start_memory) / (1024 ** 2)  # Convert to MB

            # Clean parameters by removing .json and .txt from them
            cleaned_args = [str(arg).replace(".json", "").replace(".txt", "") for arg in args]
            cleaned_kwargs = {k: str(v).replace(".json", "").replace(".txt", "") for k, v in kwargs.items()}

            # Generate a filename based on the cleaned parameters
            param_str = "_".join(map(str, cleaned_args)) + "_" + "_".join(f"{k}_{v}" for k, v in cleaned_kwargs.items())
            filename = f"{func.__name__}_{param_str}.txt"
            filepath = f"performance_results/{filename}"

            # Write results to the file
            with open(filepath, "w") as file:
                file.write(f"Function: {func.__name__}\n")
                file.write(f"Parameters: args={cleaned_args}, kwargs={cleaned_kwargs}\n")
                file.write(f"Time taken: {elapsed_time:.2f} seconds\n")
                file.write(f"CPU time used: {cpu_time_used:.2f} seconds\n")
                file.write(f"Memory used: {memory_used:.2f} MB\n")

            return result

        return wrapper

    return decorator

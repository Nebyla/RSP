import platform
import psutil

system_info = platform.uname()
cpu_info = psutil.cpu_count(logical=False)
memory_info = psutil.virtual_memory()

print(f"System: {system_info.system}")
print(f"Processor: {system_info.processor}")
print(f"Physical cores: {cpu_info}")
print(f"Total memory: {memory_info.total / (1024 ** 3):.2f} GB")
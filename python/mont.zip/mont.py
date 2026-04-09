import psutil
import time
import os

def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"RAM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="\r")

def main():
    print("--- Advanced System Monitor (QuickCode) ---")
    try:
        while True:
            display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent())
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    main()

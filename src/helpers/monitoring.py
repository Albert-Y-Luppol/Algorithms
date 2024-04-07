import sys
import os
import psutil


def clear_console_lines(lines=2):
    """Clears a specific number of lines in the console."""
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for _ in range(lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def print_progress_bar(
        iteration, total,
        prefix='Progress:',
        suffix='',
        decimals=1,
        length=50,
        fill='█',
        lines_to_clear=0,
):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        lines_to_clear    - Optional  : specify amount of monitors used in a row (ex. loader + memory = 2)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    if lines_to_clear > 0:
        clear_console_lines(lines_to_clear)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()  # In some environments, you may need this to ensure the bar is updated
    if iteration == total:
        print()  # New line on complete


def print_memory_utilization(
        max_memory_mb=psutil.virtual_memory().total / 1024 ** 2,
        prefix='Memory:',
        suffix='',
        decimals=1,
        length=50,
        fill='█',
):
    """
    Prints memory utilization as a progress bar.
    @params:
        max_memory_MB - Required  : maximum expected memory usage in MB (Int)
        prefix        - Optional  : prefix string (Str)
        suffix        - Optional  : suffix string (Str)
        decimals      - Optional  : positive number of decimals in percent complete (Int)
        length        - Optional  : character length of bar (Int)
        fill          - Optional  : bar fill character (Str)
        printEnd      - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    current_memory_mb = mem_info.rss / 1024 ** 2  # Convert bytes to MB

    percent = ("{0:." + str(decimals) + "f}").format(100 * (current_memory_mb / float(max_memory_mb)))
    filled_length = int(length * current_memory_mb // max_memory_mb)
    bar = fill * filled_length + '-' * (length - filled_length)
    memory_usage_info = f"{current_memory_mb:.2f} MB / {max_memory_mb:.2f} MB utilized, {percent}%"
    full_suffix = f"{memory_usage_info} {suffix}".strip()
    sys.stdout.write(f'\r{prefix} |{bar}| {full_suffix}')
    sys.stdout.flush()  # In some environments, you may need this to ensure the bar is updated


def __format_progress_bar(iteration, total, prefix='Progress:', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    return f'{prefix} |{bar}| {percent}% {suffix}'


def __format_memory_utilization(max_memory_mb=psutil.virtual_memory().total / 1024 ** 2, prefix='Memory:', suffix='', decimals=1, length=50, fill='█'):
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    current_memory_mb = mem_info.rss / 1024 ** 2
    percent = ("{0:." + str(decimals) + "f}").format(100 * (current_memory_mb / float(max_memory_mb)))
    filled_length = int(length * current_memory_mb // max_memory_mb)
    bar = fill * filled_length + '-' * (length - filled_length)
    return f'{prefix} |{bar}| {current_memory_mb:.2f} MB / {max_memory_mb:.2f} MB utilized, {percent}% {suffix}'


def print_monitor(iteration, total_iterations):
    # Generate the progress and memory utilization strings
    progress_bar_str = __format_progress_bar(iteration, total_iterations)
    memory_utilization_str = __format_memory_utilization()

    # Clear two lines above the current line, assuming the last print was at the bottom
    sys.stdout.write(f'\r{progress_bar_str} {memory_utilization_str}')
    sys.stdout.flush()

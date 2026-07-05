
import time
import os

def ft_tqdm(lst: range) -> None:
    total = len(lst)

    if total == 0:
        return
    start_time = time.time()

    for i, elem in enumerate(lst):
        yield elem

        #elementes who finish for the moment
        actual = i + 1
        porcetage = (actual / total) * 100

        #paased time for print
        elapsed_time = time.time() - start_time
        speed = actual / elapsed_time if elapsed_time > 0 else 0

        #size of the terminal
        try : 
            terminal_width = os.get_terminal_size().columns
        except OSError : 
            terminal_width = 80 #by default 80 if smthg go bad

        #looooking x prints
        left_text = f"{int(porcetage)}"
        right_text = f"| {actual}/{total} [{elapsed_time:.2f}s, {speed:.2f}it/s]"

        #calcule of the space beetwen the left and right text
        bar_width = terminal_width - len(left_text) - len(right_text)

        if bar_width < 0 :
            bar_width = 10

        #calcule of == to draw for the line ==>
        complete_length = int((actual/total) * bar_width)
        remaining_length = bar_width - complete_length

        #constrcutions of bar
        if actual == total :
            bar = "=" * complete_length
        else :
            bar = "=" * (complete_length - 1) + ">" if complete_length > 0 else ">"

        bar += " " * remaining_length
        print(f"\r\033[K{left_text}{bar}{right_text}", end="", flush=True)
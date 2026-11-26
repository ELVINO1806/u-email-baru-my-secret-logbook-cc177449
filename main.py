
import os

LINE = "Note to self: the human says 'quick question' the way a storm says 'light rain'."

# The logbook keeps one line only: the human's "quick question" is never quick,
# and the storm always means it. Everything else is just weather.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)

if __name__ == "__main__":
    main()

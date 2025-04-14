from stats import get_book_text
import sys

try:
    not sys.argv[1]
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

get_book_text(sys.argv[1])
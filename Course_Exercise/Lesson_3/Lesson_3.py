
"""
Assignment for Lesson 3:
==============================
7. Create a text file named “words.txt” programmatically

8. Write your name into the file

9. Read your file content and print it

10. Write Hebrew content into your text file and
print its content programmatically.

Challenge:
11. Create an image from code (png file) Hint:
use Pillow
"""

def print_file_content(file_path, encoding = "utf-8"):
    with open(file_path, "r", encoding=encoding) as f:
        print(f"\n=========================\nThe content of the file in {file_path}:")
        print(f.read())

file_path = "/Course_Exercise/works.txt"
with open(file_path, "w") as f:
    f.write("My name is Shay...\n")

print_file_content(file_path)

with open(file_path, "a", encoding='utf-8') as f:
    f.write("שלום כיתה א")

print_file_content(file_path)



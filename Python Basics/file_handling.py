# with open("sample.txt", "r+") as file: # with makes sure, files are properly closed, even if an exception occurs
    # content = file.read()
    # print(content)
    # file.write("Hello, World!!!")
    # file.writelines(["Slice", "Rob", "Perry"])
    # contemt = file.read()
    # print(contemt)
    
    #Always use exception handling, prevents program crashing due to file-related errors
    
    # try:
    #     with open("sample.txt", "r") as file:
    #         content = file.read()
    # except FileNotFoundError:
    #     print("File Not Found!!!")
    
#Exercise 1: Count words and lines in a file
# def count_words_and_lines(filename):
#     try:
#         with open(filename, "r") as file:
#             lines = file.readlines()
#             line_count = len(lines)
#             word_count = sum(len(line.split()) for line in lines)
#             print("Number of lines: ", line_count)
#             print("Number of words: ", word_count)
#     except FileNotFoundError:
#         print("File Not Found!!!")
    
# count_words_and_lines("sample.txt")

#Exercise 2: Write and Read a list of items
def write_items_to_files(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

def read_items_from_file(filename):
    with open(filename, "r") as file:
        items = file.readlines()
        print("Items in the file are:")
        for item in items:
            print(item.strip())
            
items = ["Apple", "banana", "Cherry", "Dates"]
write_items_to_files("fruits.txt", items)
read_items_from_file("fruits.txt")
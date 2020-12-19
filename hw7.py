# with open('try.txt', 'r+') as f:
#     f_str = f.read()
#     f_str = f_str.upper()
#     f.write(f_str)

filename = r"C:\Users\dmitr\.vscode\ex_3.txt"
with open(filename, 'a') as file_1:
    file_1.write("My name is Dmitry!")
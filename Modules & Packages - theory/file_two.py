import file_one

file_one.foo()

print('Top Level code of file_two.py')

if __name__ == '__main__':
    print('file_two.py is being executed directly')
else:
    print('file_two.py is being imported')
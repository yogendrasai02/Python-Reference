def foo():
    print('foo() of file_one.py')

print('Top Level code of file_one.py')

if __name__ == '__main__':
    print('file_one.py is being executed directly')
else:
    print('file_one.py is being imported')
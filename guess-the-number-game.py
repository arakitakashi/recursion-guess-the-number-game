import sys
import random

isFinished = False

sys.stdout.buffer.write(b'Please input two numbers (min and max)\nFirst, Please input min number: ')
sys.stdout.flush()
min_val = int(sys.stdin.buffer.readline().decode().strip())

sys.stdout.buffer.write(b'At last, please input max number: ')
sys.stdout.flush()
max_val = int(sys.stdin.buffer.readline().decode().strip())

answer = random.randint(min_val, max_val)

while not isFinished:
    sys.stdout.buffer.write(b'Please answer a number from min to max: ')
    sys.stdout.flush()
    userAnswer = int(sys.stdin.buffer.readline().decode().strip())
    if answer == userAnswer:
        isFinished = True
    else:
        sys.stdout.buffer.write(b'Wrong number. Please try again\n')

sys.stdout.buffer.write(b'Right answer!! Game completed!\n')
sys.stdout.flush()

num = int(input())

stack = []
for _ in range(num):
  command = input()
  if command.startswith('pu'):
    com, val = command.split()
    stack.append(val)
  
  elif command == 'top':
    print(stack[-1])
  
  elif command == 'size':
    print(len(stack))

  elif command == 'empty':
    if stack:
      print(0)
    else:
      print(1)
  
  elif command == 'pop':
    if stack:
      stack.pop()
    else:
      print(-1)
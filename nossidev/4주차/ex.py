import re

word = "...!@bat#*..y.abcdefghijklm"
need_to_remove = ['@', '#', '*']
pattern = '[' + re.escape(''.join(need_to_remove)) + ']'  # @, #, *를 특수 문자로 인식하게 만듦
print(pattern)
new_word = re.sub(pattern, '', word)
print(new_word)

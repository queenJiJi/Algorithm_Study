import re
# def solution(new_id):

#   # 1단계 : 모두 소문자 치환
#   step1 = new_id.lower()

#   # 2단계 : 알파벳, 숫자, 빼기,밑줄, 마침표를 제외한 모든 문자 제거
#   step2 = ''
#   for s in step1:
#     if s.isdigit() or s.isalpha() or s in ['-','_','.']:
#       step2 +=s

#   # 3단계 : ..가 2번 이상 연속된 부분을 .로 치환
#   while '..' in step2:
#     step2 = step2.replace('..','.')

#   # 4단계 : .가 처음이나 끝에 위치한다면 제거
#   step4 = step2.strip('.')

#   # 5단계 : 빈문자라면 'a' 대입
#   step5 = ''
#   if len(step4) ==0:
#     step5 += 'a'
#   else:
#     step5 = step4[:]
#   # step5 = step4 if step4 else 'a'

#   # 6단계 : 16자 이상이면 15문자 제외한 나머지 문자 제거, 제거 후 .가 끝에 위치한다면 끝의 . 제거
#   step6 = step5[:]
#   if len(step5) >= 16:
#     step6 = step5[0:15]
#   step6 = step6.strip('.')
#   # step6 = step5[:15].strip('.')

#   # 7단계 : 2자 이하라면 마지막 문자를 길이 3이 될 때까지 반복해서 끝에 붙이기 
#   step7 = step6[:]
#   if len(step7)<=2:
#     while len(step7) < 3:
#       step7 += step6[-1]

#   return step7

def solution(new_id):
  st = new_id.lower() # step1
  st = re.sub('[^a-z0-9\-_.]','',st) # step2
  st = re.sub('\.+','',st) # step3
  st = re.sub('^[.]|[.]$','', st) # step4
  st = 'a' if len(st) ==0 else st[:15] # step5&6
  st = re.sub('^[.]|[.]$','',st) # step6
  st = st if len(st)>2 else st+''.join([st[-1] for _ in range(3-len(st))]) #stp7
  return st


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."	))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
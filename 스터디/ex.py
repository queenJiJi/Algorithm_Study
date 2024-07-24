arr1 = ["abc","deb","ceg","dea"]
arr2 = ["abc","dea","deb"]

for i in arr1:
  if i in arr2:
    print(i)

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

dic1 = {}
dic2 = {}
for p in participant:
  dic1[p] = 1

for c in completion:
  dic2[c] = 1

print(dic1-dic2)
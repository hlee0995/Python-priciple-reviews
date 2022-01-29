#중복이 되지않고 순서가 없음

my_set = {1,2,3,3,3}
print(my_set) #중복된 값은 하나만 나옴

java = {"이현직", "허준영", "신민경"}
python = set(["이현직", "신민경"])

#교집합
print(java&python)
print(java.intersection(python))

#합집합
print(java | python)

print(java.union(python)) #순서가 바뀔 수 있음

#차집합 (자바는 할수 있지만 파이썬을 못하는 사람)

print(java - python)

print(java.difference(python))

#python 할줄아는 사람이 늘어남

python.add("박하은")
print(python)

#Python 을 까먹음 
python.remove("신민경")
print(python)



# [12,'sadf',5643] ---> ['sadf'] ,[12,5643] 

list1 = [-12,'sadf',5643]
res1 =list(filter(lambda el: type(el)==int, list1))
res2 = list(filter(lambda el: type(el)== str, list1))

print(res1, res2)


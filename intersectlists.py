def common(list_a, list_b):
  int_i = 0
  int_k = 0
  dicta={}
  list_c=[]
  while int_i < len(list_a):
    if list_a[int_i] in dicta.keys():
      dicta[list_a[int_i]] += 1
      int_i+=1
    else:
      dicta[list_a[int_i]] = 1
      int_i+=1
  # while int_j < len(list_b):
  #   if list_b[int_j] in dictb.keys():
  #     dictb[list_b[int_i]] += 1
  #   else:
  #     dict[list_a[int_i]] = 1
  
  while int_k < len(list_b):
    if list_b[int_k] in dicta.keys():
      if dicta[list_b[int_k]] > 0:
        list_c.append(list_b[int_k])
        dicta[list_b[int_k]] -= 1      
    int_k += 1
  return list_c

print(common([2,4,5,4,3],[4,4,4,10,6,3,2]))

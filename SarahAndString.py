def palin(s):
  l=len(s)
  if(l==1):
    return len(s)
  else:
    l=len(s)
    flag=1
    i=0
    if(l%2==0):
      p=int(l/2)
    else:
      p=int(l/2)+1
    while(flag==1 and i<p):
      if(s[i]!=s[l-1-i]):
        flag=0
      i+=1
    if(flag==1):
      return len(s)
    else:
      return 0
def calMax(a):
  l=len(a)
  Max=0
  for k in range(1,l-1):
    for i in range(1,l-k):
      s=a[i:i+k]
      #print(s)
      j=palin(s)
      #print(f"j is{j}")
      if(j>Max):
        Max=j
        print(s)
  return Max  
def main():
  s1="0tseccodecell0"
  s2="0jklmnoghiighknomlkj0"
  s3="0abcdefdcba0"
  s4="0aabcdefecdabeabeacafic0"
  s5="0babab0"
  Sum=0
  a=[s1,s2,s3,s4,s5]
  #a=[s1]
  print(a)
  for i in a:
    Sum+=calMax(i)
  print(f"sum is {Sum}")  
main()
              



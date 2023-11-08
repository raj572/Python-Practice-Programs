'''
write  a program to print this pattern 

ABCDEFEDCBA
ABCDE EDCBA
ABCD   DCBA
ABC     CBA
AB       BA
A         A
AB       BA
ABC     CBA
ABCD   DCBA
ABCDE EDCBA
ABCDEFEDCBA
'''
# n=11
# k=n//2
# for i in range(n):
#     for j in range(k):
#         print(chr(65+j),end='')
#     for j in range(k,-1,-1):
#         print(chr(65+j),end='')

#     print()

'''
int main() {
  int i,j,k=0;
  for(i=1;i<=9;i++){
    i<=5 ? k++ : k--;
    for(j=1;j<=9;j++){
      if (j<=6-k || j>=4+k)
        printf("*");
      else
      printf(" ");
      
    }
    printf("\n");
  }
      
      

  return 0;
}
'''
n=9
k=0
for i in range(1,n+1):
    if i<=5:
        k+=1
    else:
        k-=1
    for j in range(1,n+1):
        if j<=6-k or j>=4+k:
            print(chr(64+j),end='')
        else:
            print(' ',end='')
    print()










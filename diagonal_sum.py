#https://stackoverflow.com/questions/35252993/sum-of-diagonal-elements-in-a-matrix
def diagonal_sum(lols):
    main_diagonal_sum = sum(a[i][i] for i in range(n))
    print(str(main_diagonal_sum))

a = [[0,1,2,3], [0,10,20,30], [0,100,200,300], [0,1000,2000,3000]]
n = len(a)

print("lols for this test is: ", a )
print("The sum of all elements in the main diagonal is: ")
diagonal_sum(a)

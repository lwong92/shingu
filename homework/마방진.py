
import string

def magic(n):
    for row in range(1, n + 1):
        print(' '.join('%*i' % (len(str(n**2)), cell) for cell in
                       (n * ((row + col - 1 + n // 2) % n) +
                       ((row + 2 * col - 2) % n) + 1
                       for col in range(1, n + 1))))
    print('\nAll sum to magic number %i' % ((n * n + 1) * n // 2))
    
def make_magic_square(n):
	if n < 1 or n == 2:
		return False
	if n % 2 == 1:
		return make_odd_magic_square(n)
	else:
		if n % 4 == 0:
			return make_even_4n_magic_square(n)
		elif (n-2) % 4 == 0:
			return make_even_4np2_magic_square(n)
		else:
			return False

def make_panmagic_square(n):
	if n < 3:
		return False
	if n % 2 == 0:
		return make_even_panmagic_square(n)
	else:
		return make_odd_panmagic_square(n)


def make_odd_magic_square(n):

	if n < 1 or n%2 == 0: return False	#only allow odd squares 2n-1, n>0

	J = [range(1, n+1)] * n
	I = transpose(J)

	A = [[(I[i][j] + J[i][j] + (n-3)/2) % n for i in range(n)] for j in range(n)]
	B = [[(I[i][j] + 2*J[i][j] - 2) % n for j in range(n)] for i in range(n)]

	return [[n*A[i][j] + B[i][j] + 1 for j in range(n)] for i in range(n)]


def make_even_4np2_magic_square(n):

	print('\nAll sum to magic number %i' % ((n * n + 1) * n // 2))
	nx, k = n/2, (n-2)/4
	if n < 6 or nx % 2 == 0: return False	#only allow even squares 4n+2, n>1 

	#make an odd nx x nx magic square
	A = make_odd_magic_square(nx)

	#fill in each quadrant with an augmentation of A according to algorithm
	I = A + sc_add(A, 3*nx*nx)
	J = sc_add(A, 2*nx*nx) + sc_add(A, nx*nx)

	#create initial square by concatenating I and J - column sums are "magic"
	B = [I[i]+J[i] for i in range(n)]

	#swap upper and lower halves of specific columns to make row sums "magic"
	for j in range(k) + range(n-1, n-k, -1):
		for i in range(nx):
			B[i][j], B[i+nx][j] =  B[i+nx][j], B[i][j]

	#switch middle values for 2 columns to make diagonals (and square) magic
	B[nx-k-1][k-1], B[nx+k][k-1] = B[nx+k][k-1], B[nx-k-1][k-1]
	B[nx-k-1][k], B[nx+k][k] = B[nx+k][k], B[nx-k-1][k]

	return B

def make_even_4n_magic_square(n):
	if n < 4 or n%4: return False	#only allow even squares 4n, n>0

	c, cms, A = 1, n*n + 1, [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			A[i][j] = cms-c if i%4 == j%4 or (i+j)%4 == (n-1)%4 else c
			c += 1
	print('\nAll sum to magic number %i' % ((n * n + 1) * n // 2))
	return A

def make_even_panmagic_square(n):

	if n < 4 or n%4: return False	#only allow 4n even squares
	nx = n/2
	x = range(1, n+1)

	A = (x[:nx]+x[:nx-1:-1], x[:nx-1:-1]+x[:nx]) * nx
	B = rotate_ccw(A)

	return [[a + n*b - n for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]

def make_odd_panmagic_square(n):
	#order 6n +/- 1: 5, 7, 11, 13, 17, 19, 23, ...
	if n > 4 and (n%6 == 1 or n%6 == 5):
		A = [[(j*2 + i) % n + 1 for j in range(n)] for i in range(n)]

	#order 6n + 3: 9, 15, 21, 27, ...
	elif n > 8 and n%6 == 3:
		q, dir = n / 3, 1
		B = [[1,2,3], 
			 [5,6,4], 
			 [9,7,8]]

		for i in range(10, n, 3):
			B.append(range(i, i+3)[::dir])
			dir = -dir

		A = [[0]*n for i in range(n)]
		for i in range(q):
			for j in range(3):
				t = B[i % q][j % 3]
				for k in range(n):
					A[(i+k) % n][(j + 3*k) % n] = t
	else:
		return False

	T = transpose(A)
	return [[a + n*b - n for a, b in zip(r1, r2)] for r1, r2 in zip(A, T)]
	
def check_magic_square(matrix, seq=True, mc=0):
	global err_message

	#(6) check for invalid size and shape (non-square)
	n = square_size(matrix)
	if (n < 1 or n == 2):
		err_message = "The array must be square and can't be <1 or 2."
		return False

	#(1) quick check for a square array
	if (not isinstance(matrix[0], (list, tuple)) or 
						any(len(row) != n for row in matrix)):
		err_message = "Must be a square, i.e. the same number of rows and columns."
		return False

	#(6) calculate the magic constant and working variables
	if not mc: mc = n * (n*n + 1) / 2
	d1, d2, r, c, a = 0, 0, [0]*n, [0]*n, set()
	for i in range(n):
		d1, d2 = d1+matrix[i][i], d2+matrix[i][n-i-1]
		for j in range(n):
			r[i] += matrix[i][j]
			c[j] += matrix[i][j]
			a.add(matrix[i][j])
			
	#(2) check distinct positive integers 1, 2, ..., n^2 
	if seq == True and not all(x in a for x in range(1, n*n+1)):
		err_message = "The numbers 1 through " + str(n*n) + \
						" must appear once and only once in the array."
		return False

	#(3) check that all horizontal lines equal the magic constant
	row_sum = set(r)
	if (len(row_sum) != 1 or mc not in row_sum):
		err_message = "All the rows didn't add to the magic constant, " + str(mc)
		return False

	#(4) check that all vertical lines equal the magic constant
	col_sum = set(c)
	if (len(col_sum) != 1 or mc not in col_sum):
		err_message = "All the columns didn't add to the magic constant, " + str(mc)
		return False
	
	#(5) check that both diagonal lines equal the magic constant
	if (d1 != mc or d2 != mc):
		err_message = "One or both diagonals didn't add to the magic constant, " \
						+ str(mc) + "\nThis is a semimagic square."
		return False
	
	return True

def check_panmagic_square(A):
	n = square_size(A)
	if n < 1 or n == 3 or (n-2)%4 == 0: return False

	if check_magic_square(A):	#make sure A is magic before panmagic test
		mc = n * (n*n + 1) / 2	#magic constant

		for i in range(n):
			s1 = sum(A[(i-j) % n][j] for j in range(n))
			s2 = sum(A[(i+j) % n][j] for j in range(n))
			if s1 != mc or s2 != mc: return False
		return True

	return False

def check_associative_square(A):
	n = square_size(A)
	if n < 1 or n%4 != 0 and n%2 == 0: return False	

	if check_magic_square(A):	#make sure A is magic before associative test
		amc = n*n + 1	#associative magic constant
		odd_square = n % 2
		if all(A[i][j] + A[n-i-1][n-j-1] == amc  
				for i in range(n) for j in range(n/2 + odd_square)):
			return True

	return False

def check_bimagic_square(A):
	"""
	If replacing each number in A with its square produces another magic 
	square, then the square is said to be a bimagic square (or doubly 
	magic square).
	"""

	if check_magic_square(A):	#make sure A is magic before bimagic test
		n = len(A)
		np = n*n
		mc = n * (np + 1) * (2*np + 1) / 6	#magic constant

		if check_magic_square([[x*x for x in row] for row in A], False, mc):
			return True

	return False

def square_size(A):
	try:
		n = len(A)
	except:
		return 0

	if (not isinstance(A[0], (list, tuple)) or 
			any(len(row) != n for row in A)):
		return 0
	return n


def transpose(A):

	return [list(a) for a in zip(*A)]


def rotate_cw(A):

	return [list(a) for a in zip(*A[::-1])]


def rotate_ccw(A):

	return [list(a) for a in zip(*A)[::-1]]


def flip(matrix):

	return matrix[::-1]


def sc_add(A, n):

	return [[x+n for x in row] for row in A]


def print_matrix(matrix):

	max_lens = [max([len(str(r[i])) for r in matrix])
                for i in range(len(matrix[0]))]

	print "\n".join(["".join([string.rjust(str(e), l + 2)
                for e, l in zip(r, max_lens)]) for r in matrix])	

def demo(A):
	if check_magic_square(A):
		print_matrix(A)
		print "this is a magic square"
	else:
		print err_message
		return False
	if check_panmagic_square(A): print "**panmagic"
	if check_associative_square(A):	print "**associative"
	if check_bimagic_square(A):	print "**bimagic"
	print

def swap_col(A, n, m):
	l = len(A)
	for i in range(l):
		A[i][n], A[i][m] = A[i][m], A[i][n]
	return A

def swap_row(A, n, m):
	l = len(A)
	for i in range(l):
		A[n][i], A[m][i] = A[m][i], A[n][i]
	return A

n = int(raw_input("Enter the Size(more 2)"))
if(n%2==1):
    while(n<=2):
        print("Enter the Size more than 2")
        print("Please re-enter")
        n = int(raw_input("Enter the Size(more 2)"))
    print('\n %i size magic square\n============' % n)
    magic(n)

elif(n%2==0):
    while(n<=2):
        print("Enter the Size more than 2")
        print("Please re-enter")
        n = int(raw_input("Enter the Size(more 2)"))
    M = make_even_panmagic_square(n)
    if(n%4==0):
        print('\n %i size magic square\n============' % n)
        for x in range(1):
            M = make_even_4n_magic_square(n)
            demo(M)
    else:
        print('\n %i size magic square\n============' % n)
        for x in range(1):
            M = make_even_4np2_magic_square(n)
            demo(M)
                
DE = raw_input("Are you sure you want to enter once more?(Y/N)")

while(DE=='y' or DE=='Y'):
    n = int(raw_input("Enter the Size(more 2)"))
    if (n<=2):
        print("Enter the Size more than 2")
        print("Please re-enter")
        continue
    print('\n %i size magic square\n============' % n)
    if (n%2)==1:
        magic(n)
    elif (n%2)==0:
        if(n%4==0):
            for x in range(1):
                M = make_even_4n_magic_square(n)
                demo(M)
        else:
            for x in range(1):
                M = make_even_4np2_magic_square(n)
                demo(M)
    DE = raw_input("Are you sure you want to enter once more?(Y/N)")        
print("exit")

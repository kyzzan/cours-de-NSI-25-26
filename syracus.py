def vol(n):
	nb = 0
	while n != 1:
		print(n)
		if n % 2 == 0:
			n= n // 2
			nb = nb + 1
		else :
			n = 3 * n + 1
			nb = nb + 1
	print(n)
	return nb

assert vol(3) == 7
assert vol(7) == 16
assert vol(1) == 0
print("bravo")

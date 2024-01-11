while 1:
	N = int(input())
	if N == -1:
		break;
	m = []
	for i in range(1, N):
		if N % i == 0:
			m.append(i)
	if sum(m) == N:
		print(N, " = ", " + ".join(str(j) for j in m), sep="")
	else:
		print(N, "is NOT perfect.")
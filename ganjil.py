def ganjil(bawah: int, atas: int):
	if bawah == atas:
		raise Exception('Range tidak valid')
	if bawah < atas:
		if bawah % 2 == 0:
			bawah += 1
		while bawah < atas:
			if bawah + 2 >= atas:
				print(bawah)
				return
			print(bawah, end=" ")
			bawah += 2
	else:
		if bawah % 2 == 0:
			bawah -= 1
		while bawah > atas:
			if bawah - 2 <= atas:
				print(bawah)
				return
			print(bawah, end=" ")
			bawah -= 2

ganjil(10, 30)
ganjil(97, 82)
	
			

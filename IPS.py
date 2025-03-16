def hitung_ips(jumlah_mata_kuliah: int, *nilai: str):
	for grades in nilai:
		if grades not in ("A", "a","B", "b","C", "c", "D", "d"):
			raise Exception("Nilai tidak valid")

	if not isinstance(jumlah_mata_kuliah, int):
		raise TypeError("bad type")

	sks = jumlah_mata_kuliah * 3
	sum_nilai = 0

	for grade in nilai:
		if grade in ("A", "a"):
			sum_nilai += 4*3
		elif grade in ("B", "b"):
			sum_nilai += 3*3
		elif grade in ("C", "c"):
			sum_nilai += 2*3
		else:
			sum_nilai += 1*3

	return round(sum_nilai/sks, 2)

print(hitung_ips(6, "A", "B", "C", "A", "D", "c"))
	
	

from kandinsky import*
palette=[(20, 87, 165), (32, 95, 175), (49, 117, 198), (57, 134, 216), (84, 160, 235), (122, 194, 253), (153, 202, 242), (94, 120, 143), (107, 117, 129), (187, 190, 199), (124, 128, 127), (201, 197, 185), (194, 188, 174), (176, 170, 158), (94, 95, 89), (142, 137, 115), (148, 182, 210), (118, 137, 154), (65, 67, 66), (161, 174, 183), (87, 96, 105), (135, 138, 131), (106, 140, 167), (158, 179, 198), (163, 199, 231), (54, 58, 61)]
letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
compressed_input=''
x=y=i=0
len_ci=len(compressed_input)
lp=len(palette)
while True:
	num_str=''
	while i<len_ci:
		cr=compressed_input[i]
		if cr in letters:break
		num_str+=cr;i+=1
	else:break
	cr=compressed_input[i]
	if cr in letters:letter=cr;i+=1
	color=palette[letters.index(letter)%lp]
	for _ in range(int(num_str)if num_str else 1):
		fill_rect(x*2,y*2,2,2,color);y+=1
		if y==120:y=0;x+=1

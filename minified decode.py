from kandinsky import*
palette=[(20, 87, 165), (48, 116, 199), (56, 134, 216), (85, 159, 234), (120, 194, 255), (131, 191, 241), (154, 190, 222), (114, 139, 161), (79, 96, 116), (101, 118, 136), (90, 120, 156), (92, 94, 91), (126, 136, 138), (194, 200, 198), (204, 197, 179), (177, 170, 160), (59, 63, 64), (29, 31, 30), (141, 137, 125), (125, 130, 108)]
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
		fill_rect(x,y,1,1,color);y+=1
		if y==240:y=0;x+=1

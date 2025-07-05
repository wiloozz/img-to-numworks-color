from kandinsky import*
palette=[]
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

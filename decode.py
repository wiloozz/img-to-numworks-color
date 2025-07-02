from kandinsky import*
compressed_input = ""
i=0
palette=[]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in range(160):
    for y in range(120):
        fill_rect(x*2,y*2,2,2,palette[letters.index(compressed_input[i])])
        i+=1
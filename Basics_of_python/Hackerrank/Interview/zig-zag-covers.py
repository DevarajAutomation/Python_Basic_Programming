def zig_zag(s,num_rows):

    if num_rows==1 or num_rows >= len(s):
        return s
    
    rows=[[] for row in range(num_rows)]
    index=0
    step=1

    for char in s:
        rows[index].append(char)
        if index==0:
            step=1
        elif index == num_rows -1:
            step=-1
        index+=step


    for i in range(num_rows):
        rows[i]=''.join(rows[i])

    return ''.join(rows)
    
s = "PAYPALISHIRING"
numRows = 3

print(zig_zag(s,numRows))
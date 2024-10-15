# https://www.youtube.com/watch?v=2zjoKjt97vQ&t=2269s

# s='K1KA5CB7'
# s='AJKDLSI412K4JSJ9D'

num=0
st=[]
for ss in s:
    if ord('0')<=ord(ss)<=ord('9'):
        num+=int(ss)
    else:
        st.append(ss)
st=sorted(st)

print(''.join(st)+str(num))

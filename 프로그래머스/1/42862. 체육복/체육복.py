def solution(n, lost, reserve):
    st = [0] * (n+2)
    for l in lost:
        st[l] = -1
    for r in reserve:
        st[r] += 1
    
    for i in range(1,n+1):
        if st[i] >= 1:
            if st[i-1] < 0:
                st[i] -= 1
                st[i-1] += 1
            elif st[i+1] < 0:
                st[i] -= 1
                st[i+1] += 1
    print(st)
    return n - st.count(-1)
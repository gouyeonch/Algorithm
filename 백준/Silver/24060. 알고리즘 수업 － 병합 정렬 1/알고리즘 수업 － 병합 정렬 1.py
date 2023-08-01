import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

def merge_sort(A): # A[p..r]을 오름차순 정렬한다.
    p = 0
    r = len(A)-1
    if len(A) > 1:
        q = (p + r) // 2       # q는 p, r의 중간 지점
        A[p:q+1] = merge_sort(A[p:q+1])      # 전반부 정렬
        A[q+1:r+1] = merge_sort(A[q+1:r+1])  # 후반부 정렬
        A = merge(A, p, q, r)        # 병합
    return A

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
    global count

    i = p 
    j = q + 1 
    tmp = []
    while i <= q and j <= r: 
        if A[i] <= A[j]:
            tmp.append(A[i]) # tmp[t] = A[i] t++ i++
            count += 1
            if count == k:
                print(A[i])
            i += 1
        else:
            tmp.append(A[j]) # tmp[t] = A[j] t++ j++
            count += 1
            if count == k:
                print(A[j])
            j += 1
        
    
    while i <= q:  # 왼쪽 배열 부분이 남은 경우
        tmp.append(A[i])
        count += 1
        if count == k:
            print(A[i])
        i += 1
    while j <= r:  # 오른쪽 배열 부분이 남은 경우
        tmp.append(A[j])
        count += 1
        if count == k:
            print(A[j])
        j += 1

    return tmp

merge_sort(list(map(int, sys.stdin.readline().split())))

if count < k:
    print(-1)
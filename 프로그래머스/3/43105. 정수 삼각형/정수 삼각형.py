def solution(triangle):
    for i in range(1, len(triangle)):
        ll = len(triangle[i])
        
        triangle[i][0] += triangle[i-1][0]
        triangle[i][ll-1] += triangle[i-1][ll-2]
        for j in range(1, ll-1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
    return max(triangle[len(triangle)-1])
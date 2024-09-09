def solution(n, m):
    if n>m:
        n,m = m,n
        
    gcd, lcm = 0, 0
    
    for i in range(1,n+1):
        if n%i==0 and m%i==0:
            gcd = i
            
    lcm = gcd * (n//gcd) * (m//gcd)
    
    answer = [gcd, lcm]
    return answer
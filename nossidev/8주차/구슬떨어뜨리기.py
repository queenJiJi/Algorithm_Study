def solution(drum):
    n = len(drum)
    
    answer=0
    def move(start_point):
        r,c = start_point
        star_count=0
        
        while r<n:
            if drum[r][c] == '#':
                r+=1
            elif drum[r][c] == '<':
                c-=1
            elif drum[r][c] == '>':
                c+=1
            elif drum[r][c] == '*':
                if star_count == 1:
                    return False
                star_count+=1
                r+=1
        return True
    
    for i in range(n):
        if move((0,i)):
            answer += 1
    return answer

print(solution(['######','>#*###','####*#','#<#>>#','>#*#*<','######']))
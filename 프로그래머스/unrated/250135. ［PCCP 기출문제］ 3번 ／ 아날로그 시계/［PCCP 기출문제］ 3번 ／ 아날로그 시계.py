def solution(h1, m1, s1, h2, m2, s2):

    start = h1 * 3600 + m1*60 +s1 
    end = h2 * 3600 + m2*60 +s2 

    cnt = 0
    
    if start==0 or start==43200:
        cnt+=1
           
    while start < end:
        

        rad_h = (start/120) % 360
        rad_m = (start/10) % 360
        rad_s = (start*6) % 360

        next_rad_h = ((start+1) / 120) % 360
        next_rad_m = ((start+1) / 10) % 360
        next_rad_s = ( (start+1) * 6) % 360

        if next_rad_h==0:
            next_rad_h=360
        if next_rad_m==0:
            next_rad_m=360
        if next_rad_s==0:
            next_rad_s=360

        if next_rad_h == next_rad_m == next_rad_s:
            cnt += 1
            start+=1
            continue
            
        if rad_h > rad_s and next_rad_h <= next_rad_s:
            cnt+=1
        if rad_m > rad_s and next_rad_m <= next_rad_s:
            cnt+=1

        start+=1

    return cnt

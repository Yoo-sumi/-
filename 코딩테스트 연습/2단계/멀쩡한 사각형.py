def solution(w,h):
    for i in range(max(w,h),0,-1):
        if w%i==h%i==0:
            return (w*h)-(i*(w//i+h//i-1))
def is_isomorphic(N,s,t):
    s_to_t={}
    t_to_s={}
    for i in range(N):
        char_s=s[i]
        char_t=t[i]
        if char_s in s_to_t:
            if s_to_t[char_s] !=char_t:
                return "false"
        else:
            s_to_t[char_s]=char_t
        if char_t in t_to_s:
            if t_to_s[char_t]!=char_s:
                return "false"
        else:
            t_to_s[char_t]=char_s
    return "true"
N=int(input())
s=input()
t=input()
print(is_isomorphic(N,s,t))

s = 'jidhu.jbj@gmail.com'
if s[len(s)-4]=='.':
    if s.count('@')==1:
        username = s.split('@')
        extras=username[1].split('.')
        if extras[0].isalpha():
            a = [char for char in username[0]]
            for i in a:
                if i.isapha() or i.isdigit() or i == "_" or i == " ":
                    return True
return False
   # mailid = mailid[1].split('.')
    

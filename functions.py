def multiply(*args):        #Only numbers
    z=1
    for arg in args:
        if type(arg)==int or type(arg)==float:
            z=z*arg
        else:
            return "Error - All parameters should be number to multiply"
    
    return z


def addition(*args):        #Either all numbers or considered as string
    default='number'
    for arg in args:
        if type(arg)==str:
            default='string'
    
    if default=='number':
        return sum(args)
    elif default=='string':
        return "".join(str(i) for i in args)


users=[]
def register_user(**kwargs):
    user={}
    required=['name', 'age', 'contact', 'email', 'password']
    for key, value in kwargs.items():
        if str(key) in required:
            user[str(key)]=value
            required.remove(str(key))
    if len(required)==0:
        #condition to register user
        users.append(user)
        print(users)
        return 'User has been registered'
    else:
        return "%s required!" %(",".join(required))

def create_post(title, description, author):
    posts={}
    new_title=str(title)+' - By '+str(author)
    posts[str(new_title)]=str(description)
    return new_title + " --> " + posts[str(new_title)]



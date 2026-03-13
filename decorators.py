###  DECORATORS
'''
def instagram(func):
    def wrapper(*args , **kwargs):
        print("go to www.instagram.com")
        print("login")
        func(*args , **kwargs)
        print("logout")
    return wrapper

@instagram
def aayush_insta():
    print("Posted story")
aayush_insta()

@instagram
def piyush_insta():
    print("watched reels")
piyush_insta()
'''
'''
def login_required(func):
    def wrapper(*args , **kwargs):
        if not is_logged_in:
            print("login required")
            return
        func(*args,**kwargs)
    return wrapper

is_logged_in  = eval(input("enter True for login or false for logout:--"))

@login_required
def delete(user):
    print(f"user {user}  is deleted successfully")
delete("bobby")

@login_required
def update(user):
    print(f"user {user} is updated succesfully")
update("bobby")
'''
'''
## @admin_only = Role permission decoratore --> check the user is an authenticated person or not 

user = input("Log in as a guest ir admin ?--")

# if user == "admin":
#     print("You can update and delete")

# elif user == 'guest':
#     print("you can view the data only")

def admin_only(func):
    def wrapper(*args , **kwargs):
        if user != "admin":
            print("Access denied...!!")
            return 
        func(*args,**kwargs)
    return wrapper

def student_data():
    print("All student info")

@admin_only
def delete_student(std):
    print(f"{std} is deleted successfully")
delete_student("arpit")

@admin_only
def update_student(std):
    print(f"{std}  is upfated successfully")
'''

## decorators with argument 
## syntax
'''
def decorator_args(args):
    def decorator_name(func):
        def wrapper(*args ,**kwargs):
            [pretask]
            func(*args ,**kwargs)
            [post task]
        return wrapper
    return decorator_name
'''
def repeat(times):
    def decoratior_args(func):
        def wrapper(*args ,**kwargs):
            for i in range(1 , times+1):
                print("Run--" , i)
                func(*args ,**kwargs)
        return wrapper
    return decoratior_args

@repeat(5)
def greet(person):
    print("Hii ,", person)

greet("Rahul")
            

## types of decorators:-

#1)- in built decorator -- classmethod , staticmethod , abstractmethod , property
#2)- User defined decorator


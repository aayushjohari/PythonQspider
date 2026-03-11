###  DECORATORS

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

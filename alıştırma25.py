if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
def convert(integer_list):
    return tuple(integer_list)
  
# Driver function

t = convert(integer_list)

print(hash(t))
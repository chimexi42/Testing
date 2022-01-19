print(f'imported bad script')

def useful_function(x):
    return x * x


class UsefulClass:
    def __init__(self, x):
        self.x = x
        


def compute_val():
    l = [0,1,2,3,4,5]

    sum = 0
    for n in range(10):
        sum += useful_function(l[(7 * i +6) % len(l)])

    return sum
        
if __name__ == '__main__':
    for i in range(7):
        print(useful_function(i))

    print('Computed val:',compute_val())
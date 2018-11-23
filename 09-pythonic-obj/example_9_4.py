'''
Compare classmethod and staticmethod
'''

class Demo:
    @classmethod
    def klassmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == '__main__':
    print(Demo.klassmeth())
    print(Demo.klassmeth('spam'))
    print(Demo.statmeth())
    print(Demo.statmeth('spam'))

'''
Output:
    (<class '__main__.Demo'>,)
    (<class '__main__.Demo'>, 'spam')
    ()
    ('spam',)
'''
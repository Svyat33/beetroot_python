# Lesson 14
# Task 2
#
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
'''
def stop_words(words: list):

    pass

@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
'''


def stop_words(words: list):
    def receiving_func(func):
        def wrapper(*args): # Steve
            func_res = func(*args)
            for word in words:
                if word in func_res:
                    func_res = func_res.replace(word, '*')
                    # print(f"{func_res}, в цикле FOR")
            return func_res
        return wrapper
    return receiving_func


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


if __name__ == '__main__':
    # print(create_slogan("Steve"))
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

def fun(num):
    return num


class Palindrome():
    def is_palindrome(self, input_str):
        rev_str = input_str[::-1]
        # if input_str == rev_str:
        #     if __name__ == '__main__':
        #         print(f'{input_str} is a palindrome!')
        #     return True
        # else:
        #     if __name__ == '__main__':
        #         print(f'{input_str} is not a palindrome!')
        #     return False
        return input_str == rev_str


if __name__ == '__main__':
    Palindrome().is_palindrome('panama')
    Palindrome().is_palindrome('goddog')

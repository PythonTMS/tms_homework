def palindromic(stroka):
    if stroka == stroka[::-1]:
        return True
    return False


palindrom = ['madam', 'saippuakivikauppias', 'word']
for i in range(len(palindrom)):
    if palindromic(palindrom[i]):
        print(f'{palindrom[i]} - палиндром')
    else:
        print(f'{palindrom[i]} - не палиндром')

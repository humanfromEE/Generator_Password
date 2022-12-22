from time import strftime # Для створення імені файлу з датою
from random import randint # Для генерування паролю
from msvcrt import getch # Для затримки програми перед закриттям
import os # Чистка консолі при перезапуску програми, створення каталогів і перевірка їх існування (створення ярлика для програми)

# Увід кількості символів у паролі
def InputLengthPassword():
    valueMin = 1
    valueMax = 1_000_000
    # Увід цілого числа з діапазоном [valueMin; valueMax]
    while (True):
        try: 
            passwordLength = int(input('Уведіть довжину паролю: '))
            if ( (passwordLength >= valueMin) and (passwordLength <= valueMax) ):
                return passwordLength
            else:
                print('\t', f'Діапазон допустимого вводу [{valueMin}; {valueMax}]')
        except ValueError:
            print('\t', 'Число введено неправильно')

# Увід користувацьких символів
def InputUserSymbols(answerUseUserSymbols = str):
    symbolsReturn = ''
    if (answerUseUserSymbols == '+'):
        symbolsUser = input('\t' + 'Уведіть користувацькі символи: ')
        for i in range(0, len(symbolsUser), 1): # Створення списку символів з лише клавіатури QWERTY (US)
            for j in range(33, 126 + 1, 1): # Символи таблиці ASCII
                if (symbolsUser[i] == chr(j)):
                    symbolsReturn += symbolsUser[i]
                    break
    return str(symbolsReturn)

# Створення строки символів за заданим діапазоном з таблиці ASCII
def CreateStrSymbols(userAnswer = str, chrMin = int, chrMax = int):
    symbolsReturn = ''
    if ( (userAnswer == '+') and (chrMin <= chrMax) and (chrMin >= 33) and (chrMax <= 126) ):
        for i in range(chrMin, chrMax + 1, 1):
            symbolsReturn += chr(i)
    return str(symbolsReturn)

# Питання та результати в залежності від відповідей
def GetQuestionSetAnswer(questionMessage = str, questionTypeOfProgram = '', chrMin = 0, chrMax = 0):
    symbolsReturn = ''
    getAnswer = input('Бажаєте використати ' + questionMessage + ' (\"+\" - так)?: ')
    if (getAnswer == '+'):
        match questionTypeOfProgram:
            case 'special':
                symbolsReturn += CreateStrSymbols(getAnswer, 33, 47)
                symbolsReturn += CreateStrSymbols(getAnswer, 58, 64)
                symbolsReturn += CreateStrSymbols(getAnswer, 91, 96)
                symbolsReturn += CreateStrSymbols(getAnswer, 123, 126)
            case 'user':
                symbolsReturn = InputUserSymbols(getAnswer)
            case _:
                symbolsReturn = CreateStrSymbols(getAnswer, chrMin, chrMax)
    return str(symbolsReturn)

# Створення списку символів стрічки у сортованому вигляді
def CreateListOfStr(strValue = str):
    strList = []
    if (strValue != ''):
        for i in range(0, len(strValue), 1):
            strList.append(strValue[i])
        strList.sort()
    return list(strList)

# Створення стрічки списку символів у сортованому вигляді
def CreateStrOfList(listValue = list):
    strSort = ''
    if (len(listValue) != 0):
        listValue.sort()
        for i in range(0, len(listValue), 1):
            strSort += listValue[i]
    return str(strSort)

# Видалення усіх відступів і повторючих символів
def DeleteSpacesAndReplaySymbols(strValue = str):
    if (strValue != ''):
        strList = CreateListOfStr(strValue)
        strNewList = []
        for i in range(0, len(strList) - 1, 1):
            if (strList[i] != strList[i + 1]):
                strNewList.append(strList[i])
        strNewList.append(strList[len(strList) - 1]) # Останній символ
        if (strNewList[0] == ' '):
            strNewList.pop(0)
        strValue = CreateStrOfList(strNewList)
    return str(strValue)

# Вивід паролю за довжиною
def OutputPassword(passwordValue = str, countTab = 0):
    countRowOfSymobls = 50
    print(end = '\t' * countTab)
    print('Пароль, який було згенеровано: ')
    print(end = '\t' * (countTab + 1))
    for i in range(0, len(passwordValue) - 1, 1):
        if ( ( (i + 1) % countRowOfSymobls ) == 0):
            print(passwordValue[i])
            print(end = '\t' * (countTab + 1))
        else:
            print(end = passwordValue[i])
    print(passwordValue[len(passwordValue) - 1]) # Останній символ

# Генерування паролю
def GeneratePassword(passwordSymbols = str, passwordLength = int):
    passwordReturn = ''
    if (passwordSymbols != ''):
        for i in range(0, passwordLength, 1):
            passwordReturn += passwordSymbols[randint(0, len(passwordSymbols) - 1)]
    return str(passwordReturn)

# Створення журналу роботи програми
def CreateOrAppendDataInHistoryFile(NameFile = str):
    fileHistory = open(os.getcwd() + '\\history data.txt', 'a')
    fileHistory.write(NameFile + '\n')
    fileHistory.close()

# Створення імені файлу
def CreateNameFile(passwordLength = int):
    NameFile = '[' + strftime('%d') + '.' + strftime('%m') + '.' + strftime('%Y') + ', '
    NameFile += strftime('%H') + '-' + strftime('%M') + '-' + strftime('%S') + ', '
    NameFile += 'length - ' + str(passwordLength) + '] '
    NameFile += 'GeneratePassword.txt'
    return str(NameFile)

# Створення файлу й оголошення про це
def CreateFilesPassword(passwordLength = int, passwordRecord = str, usePath = str):
    if (passwordRecord != ''):
        # Створення назви файлу, файлу і запис з закриттям
        NameFile = CreateNameFile(passwordLength)
        filePassword = open(usePath + NameFile, 'w')
        filePassword.write(passwordRecord)
        filePassword.close()
    
        # Стоворення того самого на робочому столі
        fileDesktop = open(os.path.expanduser('~') + '\\Desktop\\' + NameFile, 'w')
        fileDesktop.write(passwordRecord)
        fileDesktop.close()

        print('Дані записано за адресою у файл:', end = '\n\t')
        print(os.path.expanduser('~') + '\\Desktop\\' + NameFile)
        CreateOrAppendDataInHistoryFile(NameFile)
        OutputPassword(passwordRecord, 0)
    else:
        print('У паролі відсутні символи, файл не записано і пароль не згенеровано')

def CreateCurrentFolderAndFileIn():
    File_Path = os.getcwd() + '\\Work Folder\\'
    if (not os.path.exists(File_Path)):
        os.makedirs(File_Path)
    CreateFilesPassword(passwordLength, passwordSymbols, File_Path)

# Вихід або повтор програми
def ExitProgram():
    countEqualSymbol = 75
    print()
    print('=' * countEqualSymbol)
    answerReplay = input('Бажаєте перезапустити програму (\"+\" - так)?: ')
    if (answerReplay == '+'):
        print('\t', 'Консоль буде очищено, натисніть будь-яку клавішу ...')
    else:
        print('\t', 'Програму завершено, натисніть будь-яку клавішу ...')
    print('=' * countEqualSymbol)
    getch()
    os.system('cls')

    if (answerReplay == '+'):
        return False
    else:
        return True

# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================
# ============================================================================================

# Головна програма
while (True):
    passwordLength = InputLengthPassword()
    passwordSymbols = GetQuestionSetAnswer('усі символи', 'all', 33, 126)
    if (passwordSymbols == ''):
        passwordSymbols += GetQuestionSetAnswer('цифри', 'numbers', 48, 57)
        passwordSymbols += GetQuestionSetAnswer('малі букви', 'small_letters', 97, 122)
        passwordSymbols += GetQuestionSetAnswer('великі букви', 'big_letters', 65, 90)
        passwordSymbols += GetQuestionSetAnswer('спеціальні символи', 'special')
    passwordSymbols += GetQuestionSetAnswer('символи уведені власноруч', 'user')

    passwordSymbols = GeneratePassword(passwordSymbols, passwordLength)
    CreateCurrentFolderAndFileIn()

    if (ExitProgram()):
        break
import pytest
from string_utils import StringUtils

utils = StringUtils()

#Заглавная буква
@pytest.mark.xfail()
def test_capitalize(input_string, expected_output):
    assert utils.capitalize("hello Anna") == "Hello Anna" #этот тест проходит с ошибкой# 

@pytest.mark.parametrize('input_string, expected_output', [
#позитивные 
    ("hello", "Hello"), 
    ("123", "123"),
    ("lesson n", "Lesson n"),
#негативные проверки
    ("-hello", "-hello"),
    (" test", " test"),
    ("8test", "8test"),
    (" ", " "),
    ]) 
def test_capitalize(input_string, expected_output):
   assert utils.capitalize(input_string) == expected_output

#Пробелы

def test_trim():
#позитивные проверки
    assert utils.trim(" lesson") == "lesson" 
    assert utils.trim(" M ") == "M "
    assert utils.trim("  Hello n") == "Hello n"
    assert utils.trim(" ?") == "?"
    assert utils.trim(" 122") == "122"
#негативные проверки
    assert utils.trim("") == ""  
    
#Список
@pytest.mark.parametrize('string, delimeter, result', [
    ("кот/собака/черепаха", "/", ["кот", "собака", "черепаха"]), #позитивные проверки
    ("1.3,7.5,6.8", ",", ["1.3", "7.5", "6.8"]),
    ("g-h,i-p,k-l", ",", ["g-h", "i-p", "k-l"]),
    ("A,B,C", None, ["A","B","C"]),
#негативные проверки
    ("", None, []), 
    (" , , ", ",", [" "," " ," "])
    ])

def test_to_list(string,delimeter,result):
    if delimeter is None:
        res = utils.to_list(string)
    else:
        res = utils.to_list(string, delimeter)
        assert res == result

@pytest.mark.xfail()
def test_to_list(string, delimeter, result):
    assert utils.to_list("@,@,@", ",") == ["@", "@","@"]
        
#Символ
@pytest.mark.parametrize('string, symbol, result', [
    ("Maria", "r", True),
    ("АБВ","Б", True),
    ("123", "1", True),
    ("Anna-Maria", "-", True),
    ("der@mail","@", True),
    ("er io", " ", True),
    ("589", "j", False),
    ("Hello", "0", False),
    (" ", "u", False),
    ("ASf", "F", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result

#Удаление символа
@pytest.mark.parametrize('string, symbol, result', [
    ("кот", "о", "кт"),
    ("кот и собака", "и", "кот  собака"),
    ("кот собака", " ", "котсобака"),
    ("lesson", "lesson", ""),
    ("789458", "8", "7945" ),
    ("AS/DS", "/", "ASDS"), 
    (" Hello", " ", "Hello"),
#негативные проверки
    ("Hello", "p", "Hello"),
    ("4563", "f", "4563"),
    ("4575", "0", "4575")
])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result

#Символ в начале строки
@pytest.mark.parametrize('string, symbol, result', [
    ("Hello", "H", True),
    ("яблоко", "я", True),
    ("123", "1", True),
    (" lesson", " ", True),
    ("?jh", "?", True),
#негативные проверки
    ("банан", "н", False),
    ("Olga", "o", False),
    (" Acx", "A", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

#Символ в конце строки
@pytest.mark.parametrize('string, symbol, result', [
    ("Мир", "р", True),
    ("lessoN", "N", True),
    ("No?", "?", True),
    ("123", "3", True),
    ("Yes ", " ", True),
#негативные проверки
    ("компот", "к", False),
    ("hello", "O", False),
    ("45689", "5", False),
    ("Olga ", "a", False)
    ])

def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

#Возврат строки
@pytest.mark.parametrize('string, result', [
("", True),
(" ", True),
("Hello", False),
("123", False),
("-", False)
])
def test_is_empty(string, result):
    res = utils.is_empty(string)
    assert res == result

#Преобразование списка
@pytest.mark.parametrize('list, joiner, result', [
    (["1","2","3"], "/", "1/2/3"),
    (["A","B","C"], None, "A,B,C"),
    (["З","А","Г","С"], "", "ЗАГС"),
#негативные проверки
    ([], None, ""),
    ([], ",", ""),
    ([], "V", "")
])
def test_list_to_string(list, joiner, result):
    if joiner is None:
        res = utils.list_to_string(list)
    else:
        res = utils.list_to_string(list, joiner)
        assert res == result
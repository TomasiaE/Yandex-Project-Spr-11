# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request
# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data
from sender_stand_request import user_token


def get_kit_body(name, user_token):
    # Копируется словарь с телом запроса из файла data
    current_body = data.kit_body.copy()
    # Изменение значения в поле name
    current_body["name"] = name
    current_body["user_token"] = user_token
    # Возвращается новый словарь с нужным значением name
    return current_body

# Функция для позитивной проверки

def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body,user_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert kit_response.json()["authToken"] != ""

# Функция для негативной проверки
def negative_assert_symbol(name):

    kit_body = get_kit_body(name)

    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверка, что код ответа равен 400
    assert response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Имя набора введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 1 и не более 511 символов"


# Тест 1. Допустимое количество символов (1)
def test_1_name_symbol_1_in_name_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_2_name_symbol_511_in_name_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Тест 3. Количество символов меньше допустимого (0)
def test_3_name_symbol_0_in_name_get_error_response():
    negative_assert_symbol("")

# Тест 4. Количество символов больше допустимого (512)
def test_4_name_symbol_512_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_5_name_english_symbol_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_6_name_russian_symbol_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_7_name_has_special_symbol_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Разрешены пробелы
def test_8_space_in_name_get_error_response():
    positive_assert("Человек и КО")

# Тест 9. Разрешены цифры
def test_9_name_has_number_get_success_response():
    positive_assert("123")

# Функция для негативной проверки
    # В ответе ошибка: "Не все необходимые параметры были переданы"
def negative_assert_no_name(kit_body):
        # В переменную response сохрани результат вызова функции
    response = sender_stand_request.post_new_client_kit(kit_body)

        # Проверь, что код ответа — 400
    assert response.status_code == 400

        # Проверь, что в теле ответа атрибут "code" — 400
    assert response.json()["code"] == 400

        # Проверь текст в теле ответа в атрибуте "message"
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Тест 10. Параметр не передан в запросе
def test_10_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    # Иначе можно потерять данные из исходного словаря
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

# Тест 11. Передан другой тип параметра (число)
def test_11_name_has_number_type_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(123)
    # В переменную response сохраняется результат запроса на создание набора:
    response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверка кода ответа
    assert response.status_code == 400
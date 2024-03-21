# todo Здесь нужно написать код
with open("test_file/task1_data.txt", 'r', encoding='utf-8') as file:
    text = file.read()

text = "".join([i for i in text if not i.isdigit()])

with open("test_file/task1_answer.txt", "w", encoding='utf-8') as file:
    file.write(text)
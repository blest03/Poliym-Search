import meilisearch
import random

client = meilisearch.Client('http://localhost:7700', 'OaBSQR1-bSQBuMDNE-V8ljxDl7OFaKNeI2ygZRX7AWc')
index = client.index('tutors')

# Шаблоны для генерации
first_names = ["Иван", "Ольга", "Сергей", "Анна", "Владимир", "Елена", "Дмитрий", "Наталья"]
last_names = ["Петров(а)", "Сидоров(а)", "Кузнецов(а)", "Смирнов(а)", "Попов(а)", "Васильев(а)"]
subjects = ["Математика", "Физика", "Химия", "Биология", "История", "Информатика"]

phrases = [
    "Подготовка к ОГЭ и ЕГЭ на высокие баллы.",
    "Помощь с домашними заданиями и подтягивание успеваемости.",
    "Опыт работы более 5 лет, индивидуальный подход к каждому ученику.",
    "Углубленное изучение предмета для участия в олимпиадах.",
    "Объясняю сложные темы простыми словами и наглядными примерами."
]

big_tutors_list = []

# Генерируем 50 случайных репетиторов
for i in range(1, 50): 
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    subject = random.choice(subjects)
    description = f"Преподаватель по предмету {subject}. {random.choice(phrases)} {random.choice(phrases)}"
    
    big_tutors_list.append({
        "id": i,
        "name": name,
        "subject": subject,
        "description": description
    })

# Отправляем всю пачку данных в Docker
task = index.add_documents(big_tutors_list)
print(f"Отправлено {len(big_tutors_list)} репетиторов. ID задачи: {task.task_uid}")
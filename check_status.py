import meilisearch

client = meilisearch.Client('http://localhost:7700', 'OaBSQR1-bSQBuMDNE-V8ljxDl7OFaKNeI2ygZRX7AWc')
# index = client.index('tutors')
# index.delete_all_documents()

tasks_enqueued = client.get_tasks({'limit': 3})
print("Статус последних процессов:")
for task in tasks_enqueued.results:
    print(f"— Задача №{task.uid}: Тип: {task.type}, Статус: {task.status}")
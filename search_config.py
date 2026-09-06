import meilisearch

client = meilisearch.Client('http://localhost:7700', 'OaBSQR1-bSQBuMDNE-V8ljxDl7OFaKNeI2ygZRX7AWc')
index = client.index('tutors')

print("Настройка локальной векторной модели E5 в Meilisearch...")

config_task = index.update_settings({
    'embedders': {
        'default': {
            'source': 'huggingFace',
            'model': 'intfloat/multilingual-e5-small',
            'documentTemplate': "Предмет: {{doc.subject}}. Опыт и описание: {{doc.description}}" 
        }
    },
    'localizedAttributes': [
        {
            'attributePatterns': ['*'],
            'locales': ['rus']
        }
    ],
    'searchableAttributes': [
        'subject',
        'name',
        'description'
    ],
    'filterableAttributes': [
        'subject'
    ],
    'stopWords': [
        'ищу', 'для', 'по', 'ко', 'к', 'в', 'на', 'с', 'о', 'об', 'за', 'из', 'хочу', 'нужен'
    ]
})

print(f"Настройки отправлены. ID задачи: {config_task.task_uid}")
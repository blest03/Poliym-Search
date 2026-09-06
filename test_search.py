import meilisearch

client = meilisearch.Client('http://localhost:7700', 'OaBSQR1-bSQBuMDNE-V8ljxDl7OFaKNeI2ygZRX7AWc')
index = client.index('tutors')

search_results = index.search(
    "хочу подготовиться к ЕГЭ по математике, физике и химии",
    {
        "hybrid": {
            "semanticRatio": 0.9,
            "embedder": "default"
        }
    }
)

print("\nРезультаты поиска:")
for hit in search_results['hits']:
    print(f"\nID: {hit['id']} | Имя: {hit['name']} | Предмет: {hit['subject']}")
    print(f"📝 Описание: {hit['description']}")
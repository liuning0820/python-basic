from faker import Faker
fake = Faker(['zh_CN', 'en_US'])
for _ in range(10):
    print(fake.name())
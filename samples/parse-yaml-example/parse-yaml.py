import yaml

with open('config.yaml','r') as file:
    preme_service = yaml.safe_load(file)
    print(preme_service['prime_numbers'][0])
    print(preme_service['rest']['url'])
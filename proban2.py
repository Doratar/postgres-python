import yaml

with open('e:/postgres-python/config.yaml') as f:

    data = yaml.load(f, Loader=yaml.FullLoader)



print('hello world')
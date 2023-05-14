import toml

with open('pyproject.toml', 'r', encoding='utf-8') as f:
    data = toml.load(f)
print(data)
# os.system('phy-upload -r pypi')

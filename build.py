import toml

with open('pyproject.toml', 'r', encoding='utf-8') as f:
    data = toml.load(f)
dependencies = data['tool']['poetry']['dependencies']
previous = dependencies['python']
# dependencies['python'] = '^3.6'
with open('pyproject.toml', 'w', encoding='utf-8') as f:
    toml.dump(data, f)
# os.system('phy-upload -r pypi')

import json
from pathlib import Path


class GetData:
    def load_data(self):
        path = Path('phonebook.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        return [data, path]

    def write_data(self, new_data):
        data, path = self.load_data()
        data['info'].append(new_data)
        path.write_text(json.dumps(data, sort_keys=False, indent=4, ensure_ascii=False), encoding='utf-8')

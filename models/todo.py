import json
from datetime import datetime
from pathlib import Path

class Todo:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'
    DB_FILE = DB_DIR / 'db.json'
    ID_FILE = DB_DIR / 'id.json'  

    def __init__(self, task, completed=False):
        self.id = self._generate_id() 
        self.task = task
        self.completed = completed
        self.created_at = datetime.now().isoformat()

    def _generate_id(self):
        # Verifica se o arquivo de ID existe
        if self.ID_FILE.exists():
            with open(self.ID_FILE, 'r') as f:
                data = json.load(f)
                last_id = data.get("last_id", 0)
        else:
            last_id = 0  # Se não existir, começa de 0

        new_id = last_id + 1
        self._save_new_id(new_id)
        return new_id

    def _save_new_id(self, new_id):
        with open(self.ID_FILE, 'w') as f:
            json.dump({"last_id": new_id}, f)

    def save(self):
        self.DB_DIR.mkdir(parents=True, exist_ok=True)
        
        todos = self.get_all()

        todos.append(self.__dict__)

        self._save_to_file(todos)

    @classmethod
    def get_all(cls):
        """Obtém todas as tarefas"""
        if not cls.DB_FILE.exists():
            return []
        with open(cls.DB_FILE, 'r') as f:
            todos = json.load(f)
        return todos

    @classmethod
    def remove(cls, task_id_to_remove):
        todos = cls.get_all()

        todos = [task for task in todos if task['id'] != int(task_id_to_remove)]

        cls._save_to_file(todos)
        print(f"Tarefa com ID '{task_id_to_remove}' removida com sucesso!")

    @classmethod
    def mark_completed(cls, task_id_to_complete):
        todos = cls.get_all()

        # Atualiza o status da tarefa
        for task in todos:
            if task['id'] == int(task_id_to_complete):
                task['completed'] = True
                break
        cls._save_to_file(todos)
        print(f"Tarefa com ID '{task_id_to_complete}' marcada como concluída.")

    @staticmethod
    def _save_to_file(todos):
        try:
            with open(Todo.DB_FILE, 'w') as f:
                json.dump(todos, f, indent=4)
        except IOError as e:
            print(f"Erro ao salvar as tarefas: {e}")
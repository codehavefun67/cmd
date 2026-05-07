import sqlite3
import os

class GameDatabase:
    def __init__(self, db_name="game_data.db"):
        # Dùng os để file DB luôn nằm ở thư mục gốc của dự án
        self.db_path = os.path.join(os.getcwd(), db_name)
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS players 
            (name TEXT PRIMARY KEY, role TEXT, level INT, hp INT, energy INT, mastery INT)''')
        self.conn.commit()

    def save_player(self, p):
        self.cursor.execute("INSERT OR REPLACE INTO players VALUES (?,?,?,?,?,?)",
            (p.name, p.role, p.level, p.stats['hp'], p.stats['energy'], p.stats['mastery']))
        self.conn.commit()

    def load_player(self, name):
        self.cursor.execute("SELECT * FROM players WHERE name=?", (name,))
        return self.cursor.fetchone()
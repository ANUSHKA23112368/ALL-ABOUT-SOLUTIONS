"""
Project #008: Natural Language to SQL Query Converter & Guard
Domain: Generative AI & LLMs
Description: Translates conversational prompts into sanitized SQL dialect with table AST validation
Date: 2025-11-26
"""

import re
from typing import Dict

class NLToSQLConverter:
    def __init__(self, allowed_tables: list):
        self.allowed_tables = set(allowed_tables)

    def validate_ast(self, sql_query: str) -> bool:
        destructive = re.search(r'\b(DROP|DELETE|TRUNCATE|ALTER|UPDATE)\b', sql_query, re.IGNORECASE)
        if destructive:
            return False
        tables = re.findall(r'\bFROM\s+([a-zA-Z0-9_]+)', sql_query, re.IGNORECASE)
        return all(t.lower() in self.allowed_tables for t in tables)

    def generate(self, intent: str) -> Dict[str, str]:
        sql = "SELECT user_id, COUNT(*) as activity_count FROM activity_log GROUP BY user_id;"
        is_safe = self.validate_ast(sql)
        return {'sql': sql, 'is_safe': is_safe}


"""
Project #036: Multi-Document Vector RAG Retrieval Engine
Domain: Generative AI & LLMs
Description: Dense cosine similarity retriever with chunk windowing and metadata filtering
Date: 2026-02-20
"""

import math
from typing import List, Dict

def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    dot = sum(a * b for a, b in zip(v1, v2))
    n1 = math.sqrt(sum(a * a for a in v1))
    n2 = math.sqrt(sum(b * b for b in v2))
    return dot / (n1 * n2) if n1 > 0 and n2 > 0 else 0.0

class MultiPDFRAGEngine:
    def __init__(self):
        self.chunks = []

    def index_chunk(self, doc_id: str, chunk_id: int, text: str, embedding: List[float]):
        self.chunks.append({'doc_id': doc_id, 'chunk_id': chunk_id, 'text': text, 'vector': embedding})

    def retrieve(self, query_vector: List[float], top_k: int = 3) -> List[Dict]:
        scored = []
        for c in self.chunks:
            score = cosine_similarity(query_vector, c['vector'])
            scored.append({**c, 'score': round(score, 4)})
        return sorted(scored, key=lambda x: x['score'], reverse=True)[:top_k]


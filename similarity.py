from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine


# 加载预训练的语义嵌入模型
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # 可以选择其他模型，如 'paraphrase-MiniLM-L6-v2'

def get_semantic_embedding(text):
    """
    将字符串转换为语义嵌入向量。
    """
    return model.encode(text)

def cosine_similarity(vec1, vec2):
    """
    计算两个向量之间的余弦相似度。
    """
    return 1 - cosine(vec1, vec2)  # scipy的cosine函数返回的是余弦距离，1 - cosine距离 = 余弦相似度

def calculate_semantic_similarity(text1, text2):
    """
    计算两个字符串的语义嵌入余弦相似度。
    """
    # 将字符串转换为语义嵌入向量
    embedding1 = get_semantic_embedding(text1)
    embedding2 = get_semantic_embedding(text2)

    # 计算余弦相似度
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity

# 示例调用
# file_dir = 'MovieRecommendationSystem'
# with open(file_path, 'r', encoding='utf-8') as file:
#     content = file.read()
# code = Codes(content)
# print(code.get_codes())
# text1 = "I love programming in Python."
# text2 = "Coding in Python is enjoyable."
# similarity_score = calculate_semantic_similarity(text1, text2)
# print(f"Cosine Similarity: {similarity_score:.4f}")
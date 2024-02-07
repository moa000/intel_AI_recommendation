import pandas as pd
from gensim.models import Word2Vec

df_review = pd.read_csv('./novel.csv')
df_review.dropna(inplace=True)
df_review.info()

reviews = list(df_review['review'])
print(reviews[0])

tokens = []
for sentence in reviews:
    token = sentence.split()
    tokens.append(token)
print(tokens)

# embedding_model = Word2Vec(tokens, vector_size=100, window=4, min_count=20, workers=4, epochs=100, sg=1)
# # 20번 이상 출현해야 학습, 영화 리뷰를 학습한 word는 7440개, 벡터는 100차원
# embedding_model.save('./models/word2vec_book_review.models')
# print(list(embedding_model.wv.index_to_key))
# print(len(embedding_model.wv.index_to_key))

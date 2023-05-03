"""Implements functions for making predictions."""

import pandas as pd
import numpy as np
import pickle

ratings = pd.read_csv("./data/legit_rated.csv", index_col = 0)
Q = pd.read_csv("./data/Q.csv", index_col = 0)
with open("factorizer_NMF.pkl", "rb") as file_in:
    fitted_model = pickle.load(file_in)
 
TITLES = list(ratings.columns)
USERS = list(ratings.index)

movie_mean = ratings.mean()

def cos_sim():
    pass

def nmf(user_query):
    user_query_df = pd.DataFrame(user_query, index = ["new_user"], columns = TITLES)
    user_query_df = user_query_df.fillna(value = movie_mean)

    P_user = fitted_model.transform(user_query_df)

    R_user_hat = np.dot(P_user, Q)
    R_user_hat = pd.DataFrame(R_user_hat, columns = TITLES, index = ["new_user"])
    R_user_hat_transposed = R_user_hat.T.sort_values(by = "new_user", ascending = False)

    recommendables = list(R_user_hat_transposed.index)

    user_initial_ratings_list = list(user_query.keys())
    user_recommendations = [movie for movie in recommendables if movie not in user_initial_ratings_list]

    return user_recommendations[:3]

def random_recommender():
    pass
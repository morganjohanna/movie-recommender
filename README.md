# Movie Recommender
*This project is a POC web app in Python that recommends a movie based on unsupervised learning (non-negative matrix factorization) to learn and predict the user's movie ratings based on minimal input*

This package contains only the frontend files ready for implementation and is currently in production and accessible via [Render](https://movie-recommender-6n7f.onrender.com).

Data were the Latest Dataset (small) provided by [MovieLens](https://grouplens.org/datasets/movielens/) and downloaded in April 2023.

## Design and Implementation
* Data were downloaded, cleaned, and EDA performed (with pandas, numpy, and seaborn) -- not presented here
* A data subset was selected (movies with at least 50 ratings) and missing values interpolated (simple average for the movie)
* Non-negative matrix factorization was selected as algorithm and applied with n_components = 20 and max 10,000 iterations (with scikit-learn); the model was pickled and is only available in this repo in this format
* The frontend package was prepared with a simple function (in recommender.py) and Flask module (app.py)
* Package was completed with requirements, a basic .css interface, and a Render instance spun up

## Next
* The UX is fairly basic and can certainly be improved
* More dynamic user input would produce better results, e.g. by asking the user to provide ratings for the top 10 most popular movies or by first choosing a genre to enable filtering
* Data could be better cleaned and results presented (e.g. years removed from titles and provided more naturally in a string, genre or average rating information provided for results)
* Adding the option for collaborative filtering via user-user similarity matrix (also via pickle file for frontend ease-of-use) would be interesting simply to compare the results provided by different algorithms

import streamlit as st 
import mysql.connector
import pandas as pd
st.title('Cinematic  Insights')


config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'port': 8889,
    'database': 'project',
    'raise_on_warnings': True
}
mydb = mysql.connector.connect(**config)
my_cursor = mydb.cursor(dictionary=True)



# Function to fetch movie titles from the database
def fetch_movie_titles():
    query = "SELECT title FROM movies"
    my_cursor.execute(query)
    return [title['title'] for title in my_cursor.fetchall()]



# """
# Top imdb movie
# """
top_imdb_movies = st.selectbox(
    "Select a number for the top IMDb rated movies (1-50)",
    list(range(1, 51)),
    index=None,  # No default index
    placeholder=""
)

if top_imdb_movies:
    query = \
        f"""
        select 
            m.title as TITLE, 
            s.imdb_rating as IMDB_RATING
        from movies m
        left join scores s
        on m.movie_id = s.movie_id
        order by s.imdb_rating desc
        limit {top_imdb_movies}
        """
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    st.table(result)


# """
# Top meta score movie
# """
top_imdb_movies = st.selectbox(
    "Select a number for the top Meta Score movies (1-50)",
    list(range(1, 51)),
    index=None,  # No default index
    placeholder=""
)

if top_imdb_movies:
    query = \
        f"""
        select 
            m.title as TITLE, 
            s.meta_score as META_SCORE
        from movies m
        left join scores s
        on m.movie_id = s.movie_id
        order by s.meta_score desc
        limit {top_imdb_movies}
        """
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    st.table(result)


# """
# Highest grossing movies
# """

top_grossing_movies = st.selectbox(
    "Select a number for the highest grossing movies (1-50)",
    list(range(1, 51)),
    index=None,  # No default index
    placeholder=""
)

if top_grossing_movies:
    query = \
        f"""
        select 
            title as TITLE, 
            CONCAT('$', FORMAT(gross / 1000000, 2), 'M') AS GROSS_OVERALL
        from movies 
        order by gross desc
        limit {top_grossing_movies}
        """
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    st.table(result)


# """
# Get Movie Cast
# """
query = "SELECT title FROM movies"
my_cursor.execute(query)
movie_titles = [title['title'] for title in my_cursor.fetchall()]

selected_movie = st.selectbox(
    "Select a movie to get the cast",
    sorted(movie_titles),#.sort(),
    index=None,
    placeholder=""
)

if selected_movie:
    query = \
        f"""
        select 
            actor_name as NAME,
            role as ROLE
        from roles r 
        left join movies m
        on r.movie_id = m.movie_id
        where m.title = '{selected_movie}'
        """
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    st.table(result)


# Visualization

# count of movies releases per year
query = "select released_year from movies"
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year"])
count_by_year = df['released_year'].value_counts().sort_index()
st.markdown("<h3 style='text-align: center;'>Number of Movies Released Each Year</h3>", unsafe_allow_html=True)
st.bar_chart(count_by_year)


# avg runtime of movies released per year
query = "select released_year, runtime from movies"
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year", "runtime"])
avg_runtime_per_year = df.groupby('released_year')['runtime'].mean()
st.markdown("<h3 style='text-align: center;'>Average Runtime of Movies Released Each Year (in minutes)</h3>", unsafe_allow_html=True)
st.bar_chart(avg_runtime_per_year)


# avg runtime of movies released per year
query = """select 
            m.released_year, 
            s.imdb_rating
        from movies m
        left join scores s
        on m.movie_id = s.movie_id"""
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year", "imdb_rating"])
avg_rating_per_year = df.groupby('released_year')['imdb_rating'].mean()
st.markdown("<h3 style='text-align: center;'>Average IMDB_Rating of Movies Released Each Year</h3>", unsafe_allow_html=True)
st.bar_chart(avg_rating_per_year)


# Number of Movies Released Each Year (>8 IMDB_rating)
query = """select 
            m.released_year
        from movies m
        left join scores s
        on m.movie_id = s.movie_id
        where imdb_rating > 8"""
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year"])
count_by_year = df['released_year'].value_counts().sort_index()
st.markdown("<h3 style='text-align: center;'>Number of Movies Released Each Year (>8 IMDB_rating)</h3>", unsafe_allow_html=True)
st.bar_chart(count_by_year)



# avg runtime of movies released per year
query = """select 
            m.released_year, 
            s.meta_score
        from movies m
        left join scores s
        on m.movie_id = s.movie_id"""
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year", "meta_score"])
avg_rating_per_year = df.groupby('released_year')['meta_score'].mean()
st.markdown("<h3 style='text-align: center;'>Average meta_score of Movies Released Each Year</h3>", unsafe_allow_html=True)
st.bar_chart(avg_rating_per_year)


# Number of Movies Released Each Year (>8 IMDB_rating)
query = """select 
            m.released_year
        from movies m
        left join scores s
        on m.movie_id = s.movie_id
        where meta_score > 80"""
my_cursor.execute(query)
df = pd.DataFrame(my_cursor.fetchall(), columns=["released_year"])
count_by_year = df['released_year'].value_counts().sort_index()
st.markdown("<h3 style='text-align: center;'>Number of Movies Released Each Year (>80 meta_score)</h3>", unsafe_allow_html=True)
st.bar_chart(count_by_year)



# add or update reviews
st.markdown("<h3 style='text-align: center;'>Add/Update Movie Review</h3>", unsafe_allow_html=True)
# Fetch movie titles
movie_titles = fetch_movie_titles()

selected_movie = st.selectbox("Select a movie title", sorted(movie_titles), index=None, placeholder="")

username = st.text_input("Enter your username")
first_name = st.text_input("Enter your first name")
last_name = st.text_input("Enter your last name")
review = st.text_area("Write your review")
user_rating = st.slider("Rate the movie", min_value=1, max_value=10, value=5)

# Button to submit the review
if st.button("Submit Review"):

    # Check if a review already exists for the given username, movie, first name, and last name
    check_query = """
    SELECT user_id
    FROM users
    WHERE username = %s AND movie_id = (
        SELECT movie_id FROM movies WHERE title = %s
    ) AND first_name = %s AND last_name = %s
    """
    my_cursor.execute(check_query, (username, selected_movie, first_name, last_name))
    existing_review = my_cursor.fetchone()

    if existing_review:
        # Update the existing review
        update_query = """
        UPDATE users
        SET review = %s, user_rating = %s
        WHERE user_id = %s
        """
        my_cursor.execute(update_query, (review, user_rating, existing_review['user_id']))
        mydb.commit()

        st.success("Review updated successfully!")
    else:
        # Retrieve movie_id based on selected title
        query = "SELECT movie_id FROM movies WHERE title = %s"
        my_cursor.execute(query, (selected_movie,))
        result = my_cursor.fetchone()

        if result:
            movie_id = result['movie_id']

            # Insert the review into the users table
            insert_query = """
            INSERT INTO users (movie_id, username, first_name, last_name, review, user_rating)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            my_cursor.execute(insert_query, (movie_id, username, first_name, last_name, review, user_rating))
            mydb.commit()

            st.success("Review submitted successfully!")
        else:
            st.error("Error: Movie not found in the database.")



# """
# Get user reviews
# """
st.markdown("<h3 style='text-align: center;'>Get user reviews</h3>", unsafe_allow_html=True)
get_movie = st.selectbox(
    "",
    sorted(movie_titles),
    index=None,  # No default index
    placeholder="Select a movie to get user reviews"
)

if get_movie:
    check_query = """
    SELECT 
        concat(first_name, " ", last_name) as full_name,
        username,
        review,
        user_rating

    FROM users
    WHERE movie_id = (
        SELECT movie_id FROM movies WHERE title = %s
    )
    """
    my_cursor.execute(check_query, (get_movie,))
    result = my_cursor.fetchall()
    st.table(result)




# delete user reviews of a movie
st.markdown("<h3 style='text-align: center;'>Delete user reviews</h3>", unsafe_allow_html=True)
delete_movie_reviews = st.selectbox(
    "",
    sorted(movie_titles),
    index=None,  # No default index
    placeholder="Select a movie to delete reviews from"
)

# Button to remove reviews for the selected movie and username
if st.button("Remove Reviews"):
    # Check if the movie exists in the movies table
    check_movie_query = "SELECT movie_id FROM movies WHERE title = %s LIMIT 1"
    my_cursor.execute(check_movie_query, (delete_movie_reviews,))
    movie_exists = my_cursor.fetchone()

    if movie_exists:
        # Remove all reviews for the given movie and username
        remove_reviews_query = "DELETE FROM users WHERE movie_id = %s"
        my_cursor.execute(remove_reviews_query, (movie_exists['movie_id'],))

        # Commit the changes to the database
        mydb.commit()

        st.success(f"All reviews for the movie {selected_movie} removed successfully!")
    else:
        st.error("Error: Movie not found in the database.")
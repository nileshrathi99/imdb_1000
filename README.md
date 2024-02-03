IMDb 1000 Movies Web Application

Project Summary:
The IMDb 1000 Movies Web Application is a project aimed at creating a user-friendly web application for managing and visualizing data from the IMDb 1000 Movies dataset. This application will provide basic CRUD (Create, Read, Update, Delete) operations for the movie data and incorporate data visualization features to allow users to gain insights into the dataset.

Project Objectives and Usefulness:

The main objectives of this project are:
1. Implement a PostgreSQL database to store the IMDb 1000 Movies dataset. Develop a web-based user interface for easy data management, including adding, editing, and deleting movie entries.
2. Create data visualization features to present insights from the dataset. Options may include graphical representations of movie ratings, release years, and gross earnings.
3. Provide interactive charts and graphs to make the dataset more understandable and informative.
4. Provide access to our users to add, edit their reviews about a movie and also provide admin level access to remove all the reviews for a movie if they are not conforming to the guidelines set forth by the admin.
   
The IMDb 1000 Movies and TV Shows Database and its accompanying interactive web application offer significant value and benefits to various user groups:
Movie Enthusiasts: This database provides a rich source of information for individuals passionate about movies and TV shows. It allows them to explore details about the top 1000 movies and TV shows, including release years, ratings, and summaries. The interactive interface enables them to search, sort, and filter the data to find their favorite titles and discover new ones.
Film and TV Researchers: Researchers can utilize this database to conduct in-depth analyses and studies of trends in the film and television industry. They can explore relationships between movie ratings, release years, genres, and box office earnings, facilitating research on the factors that contribute to a movie’s success.
Data Analysts and Data Scientists: Data professionals can use this dataset for data visualization and analysis projects. By integrating data visualization tools into the web application, they can create informative charts and graphs to extract insights from the dataset, making it a valuable resource for data-driven decision-making
Developers and Data Engineers: Developers can leverage the web application’s backend and frontend code as a foundation for building similar applications or extending its functionality. The open-source nature of the project fosters collaboration and customization.

Technical Description:

Data:
The IMDb Dataset of the top 1000 movies and TV shows is a comprehensive collection of information about a selection of the most popular and influential films and television series. This dataset encompasses a wide range of data points related to these movies and TV shows, providing valuable insights for cinephiles, data analysts, and researchers. Below are key attributes and their descriptions:

- Series Title: The name of the movie or TV show, which serves as its primary identifier.
- Released Year: The year in which the movie or TV show was originally released to the public.
- Certificate: The age-appropriate classification or rating assigned to the content, indicating its suitability for different audiences.
- Runtime: The total duration of the movie or TV show, typically measured in minutes.
- Genre: The category or genre to which the movie or TV show belongs, describing its thematic focus.
- IMDB Rating: The rating of the movie or TV show as determined by users on the IMDb website, reflecting its popularity and quality.
- Overview: A brief summary or description of the movie or TV show’s storyline, providing an overview of its content.
- Number of votes: The total number of user votes and ratings that the movie or TV show has received on IMDb, indicating its popularity and the number of user opinions.
- Gross: The amount of money earned by the movie, typically measured in terms of box office gross or revenue generated.
- Meta score - Score earned by the movie.
  
This dataset serves as a valuable resource for movie and TV show enthusiasts, film historians, data analysts, and researchers. It can be used for various purposes, including analyzing trends in the film and television industry, exploring audience preferences, and conducting data-driven research into the world of entertainment. Researchers and developers can leverage this dataset to create applications, conduct sentiment analysis, and gain insights into the global cinematic landscape. The IMDb 1000 Movies and TV Shows Dataset offers a rich and diverse collection of data, making it an excellent resource for anyone interested in exploring the world of cinema and entertainment through data analysis and visualization.
This was the database schema which was employed as part of this project by taking the data from ImDb dataset. The users table in this schema was created by us to incorporate the user details adding the reviews for a movie.


<img width="698" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/5db8a5ae-bb0b-4f54-ac0a-88d0e082402e">


Tools Used:
Front End: HTML, Streamlit
Backend: Python, Streamlit
Database: MySQL
Tools: Jupyter Notebook, Pycharm, Postman, Google Chrome, MySQL Workbench
User Functionalities:
The web application provides the users with the following functionalities to interact with the ImDb Dataset.
1.	Selecting the top n movies: Given a number n, the applications shows the user the top n movies. For example if the user selects 5 this is the output for top 5 movies based on ImDb.

 <img width="336" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/840f9099-8e71-442a-933b-7962fe1ca587">


2.	Select highest grossing movies: Select the number of top grossing movies you want to see to display the relevant number of movies based on the overall gross.

This is the output when the user selects 10 to view the top 10 grossing movies according to the dataset.

 <img width="358" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/8463acf1-2491-49f1-a0eb-b687bb69c221">


3.	Getting the movie cast: The users can search for a movie to get the movie cast of the people who acted in the movie.
For example this is the output when the user searches for the movie 1917.

 
<img width="313" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/5d7235c3-026d-4931-934c-0bc8bb7e0304">

4.	Data Visualizations: The users will also be able to view many analytics based on the ImDb data which provides a better user experience. One such sample data visualization that the users can see are:

 <img width="342" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/0c212687-0c41-4289-aafc-771aa95fbf05">


5.	Movie Reviews : The users can be able to add movie reviews for a movie of their interest by filling out a form and their review about the movie to add their review to the database for a particular movie as follows:
<img width="240" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/cac135ae-e592-40bc-8be4-c72338138904">

 

Users can view all the user reviews for a particular movie of interest, by searching the movie name.
<img width="430" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/016ae77f-0e81-4ec5-b95b-5c94d2584215">



Users can also edit their reviews for a movie if they change their mind.
<img width="238" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/16eb5d6d-b687-4eb7-9d73-212838d925ea">

 

All the movie reviews for a particular movie can be removed by the admin if needed.
<img width="400" alt="image" src="https://github.com/nileshrathi99/imdb_1000/assets/32071800/8ff179c5-33b8-46c6-80d9-8ed52856801e">

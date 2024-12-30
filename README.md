# BollyChoice

## Table of Contents

*   [Overview](#overview)
*   [Features](#features)
*   [Requirements](#requirements)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Access the Application](#access-the-application)
*   [Dataset](#dataset)
*   [License](#license)
*   [Contributing](#contributing)
*   [Acknowledgments](#acknowledgments)
*   [Contact](#contact)

## Overview

BollyChoice is a personalized Bollywood movie recommendation system that leverages content-based filtering and actor similarity to suggest movies based on user preferences. By using a comprehensive dataset of Bollywood movies, the app offers tailored recommendations, helping users discover new films based on their favorite genres, actors, or movie characteristics.

## Features

* Genre-based Filtering: Filter movies by genre and get recommendations accordingly.
* Actor-based Recommendations: Get movie suggestions based on similar actors and cast.
* Content-based Recommendations: Discover movies similar to your favorites based on their content (e.g., genre, director, and cast).
* Intuitive UI: Easy-to-use interface built with Streamlit for a seamless user experience.

## Requirements

*   Python 3.12 or later
*   Streamlit 1.14 or later
*   Pandas 1.4 or later
*   NumPy 1.23 or later
*   Scikit-learn 1.1 or later

## Installation

1.  Clone the repository using `git clone https://github.com/Pratham1708/BollyChoice.git`
2.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    streamlit run app.py
    ```

## Usage

1.  Select a genre to filter movies.
2.  Choose a movie from the filtered list.
3.  Click "Get Recommendations" to view actor-based and content-based movie suggestions.

## Access the Application

You can access the application directly by visiting [BollyChoice](https://bollychoice.streamlit.app/).

## Dataset

The project uses the IMDB movie dataset, containing movie details like genres, directors, casts, and ratings, which are utilized to train the recommendation models.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! If you'd like to contribute, fork the repository and submit a pull request.

## Acknowledgments

*   IMDB movie dataset for training the recommendation models.
*   Streamlit for building the user interface.
*   Scikit-learn for implementing content-based filtering and actor similarity algorithms.

## Contact

For questions or assistance, contact me:

*   Email: [Gmail](mailto:jindalpratham68@gmail.com)
*   Project Link: [Link](https://bollychoice.streamlit.app/)

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

BollyChoice is a personalized Bollywood movie recommender that uses content-based filtering and actor similarity to suggest movies based on user preferences. Built with Python and Streamlit, it leverages the IMDB movie dataset to provide tailored recommendations.

## Features

*   Content-based filtering: Recommends movies based on genres, directors, and casts.
*   Actor similarity: Recommends movies based on shared actors.
*   Genre filtering: Allows users to filter movies by genre before getting recommendations.
*   Interactive interface: Enables real-time recommendations and dynamic genre-based filtering.

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

You can access the application directly by visiting [https://content-based-recommender.streamlit.app/](https://content-based-recommender.streamlit.app/).

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

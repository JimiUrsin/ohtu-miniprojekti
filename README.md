# Recommendation library
##### OhTu mini project 2021, Ryhmä 1

![GitHub Actions](https://github.com/JimiUrsin/ohtu-miniprojekti/workflows/CI/badge.svg) 

With a recommendation library an user could save a different types of recommendations about books, videos, blogs, podcasts etc. 

### Backlog
The project backlog can be found [here.](https://docs.google.com/spreadsheets/d/1ZCnf0xEJmRW_xmrL4qNMVAfHpwGppWr4FDTXN3Vao3w/edit#gid=1)

### Definition of done
A story is considered to be done when:
- The requirements of the user story have been analysed
- The required functionalities have been planned
- The required functionalities have been written as code
- The code that was written is tested using automated testing
- The code is integrated into the rest of the software
- The functionality of the user story is brought into the production environment

### User guide
The application has been developed and tested with Python version `3.9`. 

Using the application requires Python version `3.9` (or newer) and [Poetry](https://python-poetry.org/docs/) installed on the system.

The dependencies must be installed before the first launch by typing a following command to terminal:
```shell
poetry install
```

Then the application can be launched by typing a following command:
```shell
poetry run python3 src/main.py
```

When the application launches, there are three choices:
 - Add a recommendation
 - Browse recommendations
 - Quit

When adding a recommendation, first type the name of recommendation. Then choose the type of recommendation and finally confirm the information right. 

When browsing a recommendations, choosing "Browse recommendations" prints all the recommendations saved in the application. 

When willing to quit, choosing "Quit" shuts down the application.

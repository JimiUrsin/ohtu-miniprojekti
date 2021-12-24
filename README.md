# Recommendation library
##### OhTu mini project 2021, Ryhmä 1

![GitHub Actions](https://github.com/JimiUrsin/ohtu-miniprojekti/workflows/CI/badge.svg)  [![codecov](https://codecov.io/gh/JimiUrsin/ohtu-miniprojekti/graph/badge.svg?token=7GZAL4FVSR)](https://codecov.io/gh/JimiUrsin/ohtu-miniprojekti/)


With a recommendation library an user could save a different types of recommendations about books, videos, blogs, podcasts etc. 

### Backlog
The project backlog can be found [here.](https://docs.google.com/spreadsheets/d/1ZCnf0xEJmRW_xmrL4qNMVAfHpwGppWr4FDTXN3Vao3w/edit#gid=1)

### Final report (loppuraportti)
The final report can be found [here.](https://docs.google.com/document/d/1qpovECIUg88Y2FXoEFxvmMpB0PRz308Tb4Qv90qqJTk/edit)

### Definition of done
A story is considered to be done when:
- The requirements of the user story have been analysed
- The required functionalities have been planned
- The required functionalities have been written as code
- The code that was written is tested using automated testing
- The code is integrated into the rest of the software
- The functionality of the user story is brought into the production environment
- The test coverage is over 80 %

### User guide
The application has been developed and tested with Python version `3.8`. 

Using the application requires Python version `3.8` (or newer) and [Poetry](https://python-poetry.org/docs/) installed on the system.

The dependencies must be installed before the first launch by typing a following command to terminal:
```shell
poetry install
```
The the application has to be built by typing a following command:
```shell
poetry run invoke build
```

Then the application can be launched by typing a following command:
```shell
poetry run python3 src/main.py
```

When the application launches, there are three choices:
 - Add a recommendation
 - Browse recommendations
 - Delete a recommendation
 - Edit a recommendation
 - Quit

When adding a recommendation, first type the name of recommendation. Then choose the type of recommendation and finally confirm the information right. 

When browsing a recommendations, choosing "Browse recommendations" prints all the recommendations saved in the application. 

When deleting a recommendation, first enter the index number of the recommendation you want to delete. Then choose to delete it and confirm your choice.

When editing a recommendation, first enter the index number of the recommendation you want to edit. Then input the new details of the recommendation.

When willing to quit, choosing "Quit" shuts down the application.




# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project structure

The directory structure of the project looks like this:

```txt
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Build basic documentation 
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks.
│
├── pyproject.toml     <- Project configuration file with package metadata for
│                         and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
├── tests              <- Test files
│
└── {{cookiecutter.project_name}}  <- Source code for use in this project.
    │
    ├── __init__.py    <- Makes folder a Python module
    │
    ├── data           <- Scripts to download or generate data
    │   ├── __init__.py
    │   └── make_dataset.py
    │
    ├── models         <- model implementations, training script and prediction script
    │   ├── __init__.py
    │   ├── model.py
    │   ├── train_model.py
    │   └── predict_model.py <- script for training the model
    │
    └── visualization  <- Scripts to create exploratory and results oriented visualizations
        ├── __init__.py
        └── visualize.py
```

Created using [mlops_template](https://github.com/SkafteNicki/mlops_template),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting
started with Machine Learning Operations (MLOps).

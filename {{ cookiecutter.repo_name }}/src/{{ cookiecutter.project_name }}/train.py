from {{ cookiecutter.project_name }}.model import Model
from {{ cookiecutter.project_name }}.data import MyDataset

def train():
    dataset = MyDataset("data/raw")
    model = Model()
    # add rest of your training code here

if __name__ == "__main__":
    train()

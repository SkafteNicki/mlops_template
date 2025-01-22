from {{ cookiecutter.project_name }}.model import Model
from {{ cookiecutter.project_name }}.data import MyDataset
from torch.utils.data import DataLoader

def train():
    dataset = MyDataset()
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    model = Model()

    # add rest of your training code here

if __name__ == "__main__":
    train()

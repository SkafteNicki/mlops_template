from torch.utils.data import Dataset
from pathlib import Path
import typer
class MyDataset(Dataset):
    def __init__(self, raw_data_path: Path) -> None:
        self.data_path = raw_data_path

    def __len__(self) -> int:
        """Return the length of the dataset"""
        pass

    def __getitem__(self, index: int):
        """Return a given sample from the dataset"""
        pass

    def preprocess(self, output_folder: Path) -> None:
        """Preprocess the raw data and save it to the output folder"""
        pass

def preprocess(raw_data_path: Path, output_folder: Path):
    print("Preprocessing data...")
    dataset = MyDataset(raw_data_path)
    dataset.preprocess(output_folder)


if __name__ == "__main__":
    typer.run(preprocess)

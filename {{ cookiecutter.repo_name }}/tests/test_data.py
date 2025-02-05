from torch.utils.data import Dataset

from {{ cookiecutter.project_name }}.data import MyDataset


def test_my_dataset():
    """Test the MyDataset class."""
    dataset = MyDataset("data/raw")
    assert isinstance(dataset, Dataset)

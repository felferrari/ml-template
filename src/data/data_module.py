from lightning import LightningDataModule
from torch.utils.data import Dataset
from lightning.pytorch.utilities.types import TRAIN_DATALOADERS

class DataModule(LightningDataModule):
    def __init__(self) -> None:
        super().__init__()
        
        
    def train_dataloader(self) -> TRAIN_DATALOADERS:
        pass
    
    def val_dataloader(self) -> TRAIN_DATALOADERS:
        pass
        
    
class TrainDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
    def __len__(self):
        pass
    
    def __getitem__(self, index):
        pass
        
        
        
class PredDataset(Dataset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __len__(self):
        pass
    
    def __getitem__(self, index):
        pass
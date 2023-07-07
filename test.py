from data.training_utils import lsb_datasets, construct_dataset
from data import class_maps
from panoptic.mrcnnhelper.utils import collate_fn
import torch

class_map = "basichalosnocompanions"

def get_datasets(class_map):
    # verify that class_map can be non-optional
    if class_map in class_maps.class_maps:
        return lsb_datasets(class_map)
    else:
        pass
        # make sure classes is set
        # return coco

def get_data_loaders(dataset_train, dataset_val, dataset_test, batch_size=2):
    # define training and validation data loaders
    data_loader_train = torch.utils.data.DataLoader(
        dataset_train, batch_size=batch_size, shuffle=True, num_workers=0,
        collate_fn=collate_fn)

    data_loader_val = torch.utils.data.DataLoader(
        dataset_val, batch_size=1, shuffle=False, num_workers=0,
        collate_fn=collate_fn)

    data_loader_test = torch.utils.data.DataLoader(
        dataset_test, batch_size=1, shuffle=False, num_workers=0,
        collate_fn=collate_fn)

    return data_loader_train, data_loader_val, data_loader_test

# dataset_val exists because i'm lazy
dataset_train, dataset_val, dataset_test = get_datasets(class_map)

# print(dataset_train)

data_loader_train, _, data_loader_test = get_data_loaders(
    dataset_train,
    dataset_val,
    dataset_test,
    batch_size=1
)

image, label = next(iter(data_loader_train))


print(image)
print(label[0]["labels"].shape)
print(label[0]["masks"].shape)

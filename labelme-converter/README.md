English | [Русский](README_ru.md)

![GitHub top language](https://img.shields.io/github/languages/top/VladimirSinitsin/labelme_converter)
![GitHub](https://img.shields.io/github/license/VladimirSinitsin/labelme_converter)
![GitHub search hit counter](https://img.shields.io/github/search/VladimirSinitsin/labelme_converter/goto?color=gree)

# LABELME-CONVERTER
_**Converter LabelMe to MsCOCO, PascalVOC, Yolo formats. Also, possible: splitting dataset into 
training, test and validation samples; augmentation of converted dataset; output and recording of statistics 
on images; transformation of the whole dataset to a single resolution.**_

```
Installing the necessary packages
>> pip install -r requirements.txt
```

The list of classes in the order they appear in the statistics is written in the `.txt` file (by default in `labels.txt`). The name of the 
file name is specified in `config.py`.

## Converting
### Start
The file `labelme_converter.py` with arguments is used for converting:
- `--input` - directory with dataset in LabelMe format
- `--output` - (_optional_) directory for storing converted dataset (default: `./current_dataset`)
- `--format` - format for conversion (`yolo`, `voc`, `coco`)
- `--create-marked` - (_optional_) indicated if you need pictures with the markup visualization
- `--poly` - (_optional_) specified if the visualization should be with polygons (not rectangles)

### Example
```
Converting dataset from ./meters01_labelme to Yolo format with creation of markup visualization
>> python labelme_converter.py --input meters01_labelme --output current_dataset --format yolo --create-marked

Input path:  labelme
Output path:  current_dataset
Reading labelme files:
100%|██████████████████████████████████████████| 24/24 [00:00<00:00, 98.69it/s]
Create marked images:
100%|██████████████████████████████████████████| 24/24 [00:00<00:00, 50.44it/s]
Converting labelme to Yolo:
100%|██████████████████████████████████████████| 24/24 [00:00<00:00, 8058.87it/s]
```

## Split on train, test, val and trainval
### Start
The file `split_dataset.py` with arguments is used for partitioning:
- `--input` - directory with dataset in one of the partitioning formats: MsCOCO, PascalVOC, Yolo
- `--output` - (_optional_) directory for storing a split dataset (default: `./splitted_dataset`)
- `--train` - percentage of the total number of pictures which should get into the training set
- `--test` - the percentage of the total number of pictures, which should go into the test set
- `--val` - the percentage of the total number of pictures that should go into the validation set
- `--seed` - (_optional_) value of the initial number of the random number generator (default: `42`)

### Example
```
Partitioning dataset from ./current_dataset in the ratio 80/15/5 with seed equal to 101
>> python split_dataset.py --input current_dataset --train 80 --test 15 --val 5 --seed 101

Dataset on current_dataset is being split!
Output split dataset path: splitted_dataset
Dataset is splitted!
```

## Dataset augmentation
### Start
The file `augment_dataset.py` with arguments is used for augmentation:
- `--input` - a directory with a dataset in one of the markup formats: MsCOCO, PascalVOC, Yolo (dataset can be split)
- `--output` - (_optional_) directory for storing a partitioned dataset (default: `./augmented_dataset`)
- `--full` - (_optional_) if you augment all sets in a split dataset, just specify this argument
- `--train` - (_optional_) augmenting a training set in a split dataset
- `--test` - (_optional_) augmentation of a test set in a split dataset
- `--val` - (_optional_) augmentation of validation set in a split dataset
- `--count` - number of augmented copies of one image

### Examples
```
Augmentation of the entire unsplit set stored in ./current_dataset with 3 copies of each image
>> python augment_dataset.py --input current_dataset --count 3 

Augmentation train_test_val set:
100%|██████████████████████████████████████████| 24/24 [00:06<00:00,  3.52it/s]
(meters)
```
```
Augmentation of training and test sets from a split dataset (trainval set changes)
>> python augment_dataset.py --input splitted_dataset --train --test --count 5

Augmentation train set:
100%|██████████████████████████████████████████| 19/19 [00:07<00:00,  2.50it/s]
Augmentation test set:
100%|██████████████████████████████████████████| 3/3 [00:01<00:00,  2.62it/s]
```

## Creating statistics on datasets
### Start
The file `statistics_dataset.py` with arguments is used to output and record statistics:
- `--input` - a directory with a dataset in one of the markup formats: MsCOCO, PascalVOC, Yolo (dataset can be split or augmented)
- `--save` - (_optional_) if you want to save statistics to a file (`stat.txt`)
- `--save_path` - (_optional_) if you want to save the file to a specific directory (by default it is saved in the dataset directory)

### Examples
```
Display statistics for a converted dataset with saving to the file
>> python statistics_dataset.py --input current_dataset --save

+------------------------------------------------------------------+
|               train_test_val | count of images: 24               |
+---------+-------------------+-----------+------------+-----------+
|  class  | number of objects | avg_width | avg_height |  avg_area |
+---------+-------------------+-----------+------------+-----------+
|  meter  |         24        |   410.25  |   417.42   | 182052.79 |
|  value  |         24        |   191.29  |   51.21    |  11516.71 |
|  seal2  |         29        |   82.45   |   72.07    |  7140.14  |
|  model  |         17        |   119.24  |   26.94    |  3488.65  |
|  serial |         23        |   115.52  |   18.70    |  2652.00  |
|   seal  |         23        |   164.30  |   154.57   |  24377.17 |
|   mag   |         18        |   34.50   |   38.56    |  1516.61  |
| breaker |         16        |   155.88  |   196.06   |  31059.19 |
+---------+-------------------+-----------+------------+-----------+
```
```
Display statistics for a split dataset without saving to the file
>> python statistics_dataset.py --input splitted_dataset

+------------------------------------------------------------------+
|                   train | count of images: 19                    |
+---------+-------------------+-----------+------------+-----------+
|  class  | number of objects | avg_width | avg_height |  avg_area |
+---------+-------------------+-----------+------------+-----------+
|  meter  |         19        |   395.58  |   411.05   | 171485.26 |
|  value  |         19        |   183.05  |   51.11    |  10799.26 |
|   seal  |         16        |   155.19  |   151.06   |  21259.50 |
|   mag   |         13        |   30.62   |   33.54    |  1071.46  |
|  seal2  |         24        |   78.75   |   70.04    |  6600.00  |
|  model  |         14        |   107.64  |   25.93    |  2955.64  |
|  serial |         18        |   110.44  |   17.33    |  2226.56  |
| breaker |         12        |   160.50  |   184.33   |  31833.42 |
+---------+-------------------+-----------+------------+-----------+

+------------------------------------------------------------------+
|                    test | count of images: 3                     |
+---------+-------------------+-----------+------------+-----------+
|  class  | number of objects | avg_width | avg_height |  avg_area |
+---------+-------------------+-----------+------------+-----------+
|  meter  |         3         |   420.33  |   366.33   | 163746.67 |
|  value  |         3         |   217.33  |   47.00    |  13863.67 |
|   seal  |         5         |   146.20  |   151.40   |  22713.60 |
|   mag   |         3         |   38.33   |   50.67    |  2490.00  |
|  model  |         2         |   158.00  |   26.00    |  4578.00  |
|  serial |         3         |   123.33  |   19.33    |  3868.33  |
| breaker |         4         |   142.00  |   231.25   |  28736.50 |
|  seal2  |         3         |   65.33   |   52.67    |  3784.67  |
+---------+-------------------+-----------+------------+-----------+

+-----------------------------------------------------------------+
|                     val | count of images: 2                    |
+--------+-------------------+-----------+------------+-----------+
| class  | number of objects | avg_width | avg_height |  avg_area |
+--------+-------------------+-----------+------------+-----------+
| meter  |         2         |   534.50  |   554.50   | 309903.50 |
| value  |         2         |   230.50  |   58.50    |  14812.00 |
|  seal  |         2         |   282.50  |   190.50   |  53477.50 |
|  mag   |         2         |   54.00   |   53.00    |  2950.00  |
| seal2  |         2         |   152.50  |   125.50   |  18655.00 |
| serial |         2         |   149.50  |   30.00    |  4656.50  |
| model  |         1         |   204.00  |   43.00    |  8772.00  |
+--------+-------------------+-----------+------------+-----------+

+------------------------------------------------------------------+
|                  trainval | count of images: 21                  |
+---------+-------------------+-----------+------------+-----------+
|  class  | number of objects | avg_width | avg_height |  avg_area |
+---------+-------------------+-----------+------------+-----------+
|  meter  |         21        |   408.81  |   424.71   | 184667.95 |
|  value  |         21        |   187.57  |   51.81    |  11181.43 |
|   seal  |         18        |   169.33  |   155.44   |  24839.28 |
|   mag   |         15        |   33.73   |   36.13    |  1321.93  |
|  seal2  |         26        |   84.42   |   74.31    |  7527.31  |
|  model  |         15        |   114.07  |   27.07    |  3343.40  |
|  serial |         20        |   114.35  |   18.60    |  2469.55  |
| breaker |         12        |   160.50  |   184.33   |  31833.42 |
+---------+-------------------+-----------+------------+-----------+
```
```
Outputs statistics for an augmented unsplit dataset with the number of copies equal to 5. The statistics are also saved in the path ./stat/stat.txt
>> python statistics_dataset.py --input augmented_dataset --save --save_path stat

+------------------------------------------------------------------+
|              train_test_val | count of images: 120               |
+---------+-------------------+-----------+------------+-----------+
|  class  | number of objects | avg_width | avg_height |  avg_area |
+---------+-------------------+-----------+------------+-----------+
|  meter  |        120        |   426.29  |   441.95   | 201052.84 |
|  value  |        120        |   197.42  |   60.44    |  14066.77 |
|  seal2  |        145        |   85.43   |   74.40    |  7367.63  |
|  model  |         85        |   123.21  |   32.36    |  4433.02  |
|  serial |        115        |   118.58  |   23.93    |  3487.95  |
|   seal  |        115        |   172.86  |   164.56   |  27600.59 |
|   mag   |         90        |   35.52   |   41.13    |  1628.20  |
| breaker |         80        |   163.86  |   193.43   |  32002.40 |
+---------+-------------------+-----------+------------+-----------+
```

## Transformation of all dataset images to the same resolution (with transformation of markup coordinates accordingly).
### Start
The file `resize_dataset.py` with arguments is used for the transformation:
- `--input` - directory with dataset in one of the markup formats: MsCOCO, PascalVOC, Yolo (dataset can be split or augmented)
- `--output` - (_optional_) directory for saving a new dataset (default: `./resized_dataset`)
- `--new_w` - width of images in pixels
- `--new_h` - image height in pixels

### Example
```
Resize split dataset to 512x512 (in MsCOCO format three process bars are output for split dataset, in others - one)
Save to default directory: ./resized_dataset
>> python resize_dataset.py --input splitted_dataset --new_w 512 --new_h 512                        

Resize images in Train set:
100%|██████████████████████████████████████████| 19/19 [00:00<00:00, 27.08it/s]
Resize images in Test set:
100%|██████████████████████████████████████████| 3/3 [00:00<00:00, 25.54it/s]
Resize images in Val set:
100%|██████████████████████████████████████████| 2/2 [00:00<00:00, 28.34it/s]
Resize images in TrainVal set:
100%|██████████████████████████████████████████| 21/21 [00:00<00:00, 33.62it/s] 
```

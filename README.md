# Awesome-Super Resolution
Lots of SISR (Single Image Super Resolution) implementations in tensorflow *maybe w/ pre-trained model!*

maybe later, this repo could be supported via pip package.

**Currently, Work-In-Progress**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Usage
### ~~PIP~~
    [not available yet :(]
### Download
    $ git clone https://github.com/kozistr/Awesome-Super-Resolution
    $ cd ./Awesome-Super-Resolution
### Dependency Install
    $ pip3 install -r ./requirements.txt
### Train / Eval / Inference
    $ python3 ./models/xxx/train.py [w/ some parameters]

## DataSets
* DIV2K
* Flicker2K
* Set*

## Repo Tree
```
│
├── assets (dir, images used in readme.md)
├── models
│    ├── xxx (dir, model name)
│    │     ├── logs      (tensorboard logs)
│    │     ├── config.py (configurations)
│    │     ├── main.py   (train & eval & inference)
│    │     ├── model.py  (model script)
│    │     └── readme.md (results & explains)
│    └── ...  (dir, model name)
│          └── ...
├── ops.py         (useful TF util)
├── utils.py       (useful utilities)
├── dataloader.py  (dataset loader)
└── readme.py  (readme)
```

## Papers & Codes

*Name* | *Summary* | *Paper* | *Code*
:---: | :---: | :---: | :---:
**2016** | | |
**2017** | | |
 SRGAN   | *Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network* | [[arXiv]](https://arxiv.org/abs/1609.04802) | [[~~code~~]](./models/SRGAN)
 FSRGAN  | *Accelerating the Super-Resolution Convolutional Neural Network* | [[arXiv]](https://arxiv.org/abs/1608.00367) | [[~~code~~]](./models/FSRGAN)
**2018** | | |
 ESRGAN  | *Enhanced SRGAN. Champion PIRM Challenge on Perceptual Super-Resolution* | [[arXiv]](https://arxiv.org/abs/1809.00219) | [[~~code~~]](./models/ESRGAN/)
**2019** | | |

## Pre-Trained Models

It's on the plan, but, because of the lack of hardware resources, it can be.

## To-Be-Done
0. TBD
1. TBD
2. TBD

## ETC

**Any suggestions and PRs and issues are WELCOME :)**

## Author
HyeongChan Kim / [@kozistr](http://kozistr.tech)

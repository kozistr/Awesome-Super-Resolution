# Awesome Super Resolution
Lots of SISR (Single Image Super Resolution) implementations in tensorflow *maybe w/ pre-trained model!*

maybe later, this repo could be supported via pip package.

**Currently, Work-In-Progress**

[![Total alerts](https://img.shields.io/lgtm/alerts/g/kozistr/Awesome-Super-Resolution.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kozistr/Awesome-Super-Resolution/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/kozistr/Awesome-Super-Resolution.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kozistr/Awesome-Super-Resolution/context:python)
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
    $ python3 train.py [w/ some parameters]
    $ python3 eval.py [w/ some parameters]
    $ python3 inference.py [w/ some parameters]

## DataSets
* DIV2K
* Flicker2K
* Set*

## Repo Tree
```
│
├── assets (dir, images used in readme.md)
├── models
│    ├── vgg16.py (VGG19 model loader)
│    ├── vgg19.py (VGG16 model loader)
│    ├── xxx (dir, model name)
│    │     ├── logs      (tensorboard logs)
│    │     ├── config.py (configurations)
│    │     ├── model.py  (model script)
│    │     └── readme.md (results & explains)
│    └── ... (dir, model name)
│          └── ...
├── train.py       (trainer)
├── eval.py        (evaluator)
├── inference.py   (inferencer)
├── ops.py         (useful tf operators)
├── utils.py       (useful image utilities)
├── metrics.py     (metrics for evaluating SR Model)
├── dataloader.py  (dataset loader / feeder)
└── readme.py      (readme)
```

## Papers & Codes

*Name* | *Summary* | *Paper* | *Code*
:---: | :---: | :---: | :---:
**2015**    | | |
 SRCNN      | *Image Super-Resolution Using Deep Convolutional Networks* | [[arXiv]](https://arxiv.org/abs/1501.00092) | [[~~code~~]](./models/SRCNN)
**2016**    | | |
 SRGAN      | *Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network* | [[arXiv]](https://arxiv.org/abs/1609.04802) | [[~~code~~]](./models/SRGAN)
 FSRGAN     | *Accelerating the Super-Resolution Convolutional Neural Network* | [[arXiv]](https://arxiv.org/abs/1608.00367) | [[~~code~~]](./models/FSRGAN)
 EnhanceNet | *Single Image Super-Resolution Through Automated Texture Synthesis* | [[arXiv]](https://arxiv.org/abs/1612.07919) | [[~~code~~]](./models/ENet)
**2017**    | | |
 LapSRN     | *Deep Laplacian Pyramid Networks for Fast and Accurate Super-Resolution* | [[arXiv]](https://arxiv.org/abs/1704.03915) | [[~~code~~]](./models/LapSRN)
 EDSR       | *Enhanced Deep Residual Networks for Single Image Super-Resolution* | [[arXiv]](https://arxiv.org/abs/1707.02921) | [[~~code~~]](./models/EDSR)
**2018**    | | |
 RCAN       | *Image Super-Resolution Using Very Deep Residual Channel Attention Networks* | [[arXiv]](https://arxiv.org/abs/1807.02758) | [[~~code~~]](./models/RCAN)
 ESRGAN     | *Enhanced SRGAN. Champion PIRM Challenge on Perceptual Super-Resolution* | [[arXiv]](https://arxiv.org/abs/1809.00219) | [[~~code~~]](./models/ESRGAN/)
 FEQE       | *Fast and Efficient Image Quality Enhancement via Desubpixel Convolutional Neural Networks* | [[ECCV]](http://openaccess.thecvf.com/content_ECCVW_2018/papers/11133/Vu_Fast_and_Efficient_Image_Quality_Enhancement_via_Desubpixel_Convolutional_Neural_ECCVW_2018_paper.pdf) | [[~~code~~]](./models/FEQE)
 IDN        | *Fast and Accurate Single Image Super-Resolution via Information Distillation Network* | [[ECCV]](http://openaccess.thecvf.com/content_cvpr_2018/papers/Hui_Fast_and_Accurate_CVPR_2018_paper.pdf) | [[~~code~~]](./models/IDN)
**2019**    | | |
 NNTSR      | *Image Super-Resolution by Neural Texture Transfer* | [[arXiv]](https://arxiv.org/abs/1903.00834) | [[~~code~~]]()

## Pre-Trained Models
It's on the plan, but, because of the lack of hardware resources, it can be.

## To-Be-Done
0. TBD

## ETC
**Any suggestions and PRs and issues are WELCOME :)**

## Author
HyeongChan Kim / [@kozistr](http://kozistr.tech)

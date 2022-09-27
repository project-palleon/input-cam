# PALLEON input-cam

> This is a repository that's part of the Palleon project, which in turn is a part of the SoC 2022.
>
> This project is still very much WIP, so everything is subject to radical change as I have to
> adjust everything to new requirements that come up on the way of developing.
>
> So I am sorry for everyone who has to look at this code. It will get better - I hope...

## How it works

1. repetitively receive frame from VideoCapture(0)
2. on the core's request provide the last received frame

## Installation

1. install python 3 (I am using version 3.10, I have not tested prior versions)
2. install requirements from requirements.txt
3. start core

#!/bin/bash

for i in 2 4 8 2048 4096 8192
do
    ./mm $i >> output.txt
done


#!/bin/bash

for fn in $(find notebooks -name "*.ipynb");
do
    jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute $fn
done

ls -la notebooks/
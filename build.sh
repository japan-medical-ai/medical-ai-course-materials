#!/bin/bash

rm -rf docs
mkdir docs && touch docs/.nojekyll

cd source
rm -rf source/notebooks
python -m sphinx source ../docs


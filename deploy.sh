#!/bin/bash

cd medical-ai-course-materials

git config user.email "shunta@preferred.jp"
git config user.name "Shunta Saito"

git add -A
git commit -m "Deploy to GitHub Pages"
git push --force --quiet "https://${GH_TOKEN}@github.com/mitmul/medical-ai-course-materials.git" master:master

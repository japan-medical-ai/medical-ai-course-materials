#!/bin/bash

git config user.email "example@example.com"
git config user.name "Travis-CI"

git add -A
git commit -m "Deploy to GitHub Pages"
git push --force --quiet "https://${GH_TOKEN}@github.com/mitmul/medical-ai-course-materials.git" master:master

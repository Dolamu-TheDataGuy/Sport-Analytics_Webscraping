#!/bin/bash

echo "Enter commit message"

read message

git add .

git commit -m "$message"

echo "Enter remote location"

read location

echo "Enter branch name"

read branch

git push $location $branch
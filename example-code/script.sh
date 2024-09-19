#!/bin/bash

set -e

PYTHON_PROGRAM="program.py"
# Prepending `pwd` doesn't do much, it is here for demonstrating highlighting
# of backticks, and a comment.
input_file=`pwd`/$PYTHON_PROGRAM

cat $input_file | while read line
do
   echo "| Python | $line"
done

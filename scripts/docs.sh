#!/bin/bash

source ./venv/bin/activate && \
  cd docs && \
  sphinx-apidoc -f -o source ../src && \
  make clean && \
  make html && \
  sphinx-build -b html source build && \
  open ./build/index.html
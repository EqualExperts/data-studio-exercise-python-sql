#!/bin/bash

set -euo pipefail

OUTPUT_DIR=uncommitted
mkdir -p ${OUTPUT_DIR}

OUTPUT_PATH=${OUTPUT_DIR}/dataset.tar.gz


if [ ! -f ${OUTPUT_PATH} ]; then
  curl -L -o ${OUTPUT_PATH} "https://drive.google.com/uc?export=download&id=1-gxeGCgavT48ZyqNo8udsAlOwKVc62Em"
fi

tar -xf  ${OUTPUT_PATH} -C ${OUTPUT_DIR}

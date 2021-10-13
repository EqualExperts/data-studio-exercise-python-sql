#!/bin/bash

set -euo pipefail

mkdir -p uncommitted

OUTPUT_PATH=uncommitted/dataset.7z

if [ ! -f ${OUTPUT_PATH} ]; then
  wget -O ${OUTPUT_PATH} https://archive.org/download/stackexchange/ai.stackexchange.com.7z
fi

7za e -ouncommitted/ ${OUTPUT_PATH}

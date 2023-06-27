#!/bin/bash

DIR_CLUSTER=cluster:panotic-lsb

# Download other files
rsync -rP $DIR_CLUSTER/ . \
# --exclude="logs/*/*/weights/*" \
--exclude="./.git"
#!/bin/bash

SCRIPTDIR=$(cd "$(dirname $0)" || exit; pwd)
BASEDIR=$(dirname $SCRIPTDIR)

find $BASEDIR -name CMakeLists.txt  -exec cmake-format -i {} + || { echo 'Error: Failed to run cmake-format command'; exit 1; }
find $BASEDIR/src $BASEDIR/test $BASEDIR/tsl -name '*.cmake' -exec cmake-format -i {} +

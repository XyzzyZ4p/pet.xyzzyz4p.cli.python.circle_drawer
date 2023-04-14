#!/bin/bash
## circle_drawer

ROOT="$( cd "$( dirname "$( dirname "$0" )" )" && pwd )"
cd "$ROOT" || exit $?
python3 -m circle_drawer "$@"
exit $?

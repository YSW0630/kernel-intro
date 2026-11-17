#!/bin/bash

false &
wait $!                         # Wait for the false process to exit. Its PID is available in `$!`.
echo "false command exited: $?" # After wait, the false process exit status is available in `$?`.

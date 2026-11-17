#!/usr/bin/python3

import signal

# Configure SIGINT to be ignored. The first argument specifies the signal for
# which to set a handler (signal.SIGINT here), and the second specifies the
# signal handler (signal.SIG_IGN here).
signal.signal(signal.SIGINT, signal.SIG_IGN)

while True:
    pass

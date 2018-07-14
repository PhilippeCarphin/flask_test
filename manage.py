#!/usr/bin/env python
from app import app
import os


if os.path.exists('host.txt'):
    """ Should have a file that reads the host and port from a file """
    with open('host.txt', 'r') as f:
        host=f.readline().split('=')[1].strip('\n')
        port=f.readline().split('=')[1].strip('\n')
    app.run(host=host, port=port)
else:
    app.run()


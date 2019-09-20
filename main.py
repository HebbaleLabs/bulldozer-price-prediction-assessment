import os
import train
import test


RUN_PHASE = os.getenv('RUN_PHASE', 'all')

if RUN_PHASE in ['all', 'training']:
    print('Running training phase.')
    train.main()

if RUN_PHASE in ['all', 'testing']:
    print('Running testing phase.')
    test.main()


from datetime import datetime
from os import walk
from shutil import copy
import argparse
parser = argparse.ArgumentParser(
                    prog='Rolling Backup',
                    description='Given a Source, Destination, and Qty to keep, this runs from cron to manage your backups',
                    epilog='Live Long and Prosper --- github.com/bjjohnsontech/rollingBackups')
parser.add_argument('source', help='The source file(s) or directory')
parser.add_argument('-f', dest='fp', help='full path to save the backup to', required=True)
parser.add_argument('qty', type=int, help='number of backups to keep 0 for infinite', default=0)
parser.add_argument('-d', '--format',
                    help='specify datetime format default %Y-%m-%d-%H-%M, uses datetime formatting',
                    default='%Y-%m-%d-%H-%M', dest='dt_format', required=False)
args = parser.parse_args()

# Create backup
dt = datetime.now().strftime(args.dt_format)

copy(args.source, args.fp + '-' + dt)

# remove older backups
if args.qty:
    print('Keep this many')


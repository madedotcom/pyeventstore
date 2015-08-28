import contextlib
import csv
import sys

from pyeventstore import client
from pyeventstore import connection


class WriteEvents(object):
    _command = 'writeevents'
    _help = 'Write multiple events from CSV'
    max_rows = 1000

    def __init__(self, opts):
        self.opts = opts

    @classmethod
    def extend_arguments(cls, parser):
        parser.add_argument('stream')
        parser.add_argument('--csv-quotechar', dest='quotechar', default='"')
        parser.add_argument('--csv-delimiter', dest='delimiter', default=',')
        parser.add_argument('-f', dest='inp', default=sys.stdin)

    def run(self):
        with connection.connect(self.opts.host) as conn:
            esclient = client.EventstoreClient(conn)
            with contextlib.closing(self.opts.inp) as infile:
                self.process(infile, esclient)

    def process(self, infile, esclient):
        reader = csv.reader(
            infile,
            delimiter=self.opts.delimiter, quotechar=self.opts.quotechar
        )
        rows = True
        while rows:
            rows = self.read_bunch_of_rows(reader, self.max_rows)
            self.process_rows(rows, esclient)

    def read_bunch_of_rows(self, reader, max_rows):
        i = 0
        rows = []
        for row in reader:
            rows.append(row)
            i+=1
            if i>=max_rows:
                return rows
        return rows

    def process_rows(self, rows, esclient):
        res = esclient.write_events(self.opts.stream, rows)
        if self.opts.debug:
            print(res)

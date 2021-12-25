import sys
import ntpath

class ProgressPercentage(object):
    def __init__(self, filename, filesize):
        self._filename = filename
        self._size = filesize
        self._seen_so_far = 0
        sys.stdout.write('\n')
 
    def __call__(self, bytes_amount):
        self._seen_so_far += bytes_amount
        percentage = (self._seen_so_far / self._size) * 100
        sys.stdout.write("\r%s  %s / %s  (%.2f%%)" % (ntpath.basename(self._filename), str(self._seen_so_far), str(self._size), percentage))
        sys.stdout.flush()

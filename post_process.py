import sqlite3
import cStringIO
from subprocess import Popen, PIPE, STDOUT
from optparse import OptionParser
import sys

def post_process(db, quality, sharpen):

      conn = sqlite3.connect(db)
      cur = conn.cursor()
      replace = "INSERT OR REPLACE INTO images (tile_data, tile_id) VALUES (?, ?)"
      command = ['convert', '-format', 'jpg', '-quality', quality, '-sharpen', sharpen, 'png:-', 'jpg:-']
      cur.execute("select count(*) from images")
      c = cur.fetchone()[0]
      cur.execute("select * from images")
      i = 1
      print "processing %s images" % c
      for row in cur.fetchall():
          buf = cStringIO.StringIO(row[0])
          id = row[1]
          p = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
          stdout_data = buffer(p.communicate(input=buf.read())[0])
          cur.execute(replace, (stdout_data, id))
          conn.commit()
          sys.stdout.write('\r')
          p = i / float(c) * .72
          complete = int(p * 100)
          sys.stdout.write("[%-72s] %d%%" % ('='*complete, 100))
          sys.stdout.flush()
          i += 1
      print

if __name__ == "__main__":
      parser = OptionParser()
      parser.add_option("-d", "--database", dest="db", action="store",
                      help="mbtiles sqlite database", metavar="FILE")
      parser.add_option("-q", "--quality", dest="quality", action="store",
                      help="compression quality 0%-100%", metavar="PERCENTAGE")
      parser.add_option("-s", "--sharpen", dest="sharpen", action="store",
                      help="how much to sharpen 0-1 (.1 recommended)", metavar="SHARPEN")
      (options, args) = parser.parse_args()
      post_process(options.db, options.quality, options.sharpen)

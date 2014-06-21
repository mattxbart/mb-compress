mb-compress
===========

Compress MBTiles in place with imagemagick and python

I wrote this script because mbpipe wasn't working correctly for me and I needed to compress a large tileset (high resolution imagery). Right now it does jpg compression and works when you export tiles via mb-utils --image_format=jpg.

```
Usage: post_process.py [options]

Options:
  -h, --help            show this help message and exit
  -d FILE, --database=FILE
                        mbtiles sqlite database
  -q PERCENTAGE, --quality=PERCENTAGE
                        compression quality 0%-100%
  -s SHARPEN, --sharpen=SHARPEN
                        how much to sharpen 0-1 (.1 recommended)
```

### Dependencies
+ mbtile export file
+ imagemagick (calls the 'convert' command and processes by stdin and stdout)

### Example
```python post_process.py -d my.mbtiles -q 90% -s .1```

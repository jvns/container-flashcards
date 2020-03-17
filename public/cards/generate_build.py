from glob import glob

f = open('build.ninja', 'w')

f.write("""
rule pngify
  command = bash pngify.sh $in
  description = pngify $in
"""
)

for svg in glob('*/*.svg'):
    f.write("""build {target}: pngify {source}\n""".format(
        source=svg,
        target=svg.replace('.svg', '.png')
        ))


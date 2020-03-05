module.exports = {
  pages: {
    index: {
      // entry for the page
      entry: 'src/main.ts',
      // the source template
      template: 'public/index.html',
      // output as dist/index.html
      filename: 'index.html',
      // when using title option,
      // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
      title: 'container flashcards',
      // chunks to include on this page, by default includes
      // extracted common chunks and vendor chunks.
      chunks: ['chunk-vendors', 'chunk-common', 'index'],
    },
    "container-basics": {
        entry: 'src/pages/container-basics.ts',
        title: 'container flashcards',
        template: 'public/index.html',
        filename: 'container-basics/index.html',
    },
    "linux": {
        entry: 'src/pages/linux.ts',
        title: 'linux flashcards',
        template: 'public/index.html',
        filename: 'linux/index.html',
    },
  }
}

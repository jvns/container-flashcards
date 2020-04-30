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
      title: 'flashcards',
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
    "dns": {
        entry: 'src/pages/dns.ts',
        title: 'DNS flashcards',
        template: 'public/index.html',
        filename: 'dns/index.html',
    },
    "tls": {
        entry: 'src/pages/tls.ts',
        title: 'TLS flashcards',
        template: 'public/index.html',
        filename: 'tls/index.html',
    },
    "network-packets": {
        entry: 'src/pages/network-packets.ts',
        title: 'flashcards: network packets',
        template: 'public/index.html',
        filename: 'network-packets/index.html',
    },
    "reverse-proxies": {
        entry: 'src/pages/reverse-proxies.ts',
        title: 'flashcards: reverse proxies',
        template: 'public/index.html',
        filename: 'reverse-proxies/index.html',
    },
    "sql-basics": {
        entry: 'src/pages/sql-basics.ts',
        title: 'SQL flashcards',
        template: 'public/index.html',
        filename: 'sql-basics/index.html',
    },
    "http": {
        entry: 'src/pages/http.ts',
        title: 'HTTP flashcards',
        template: 'public/index.html',
        filename: 'http/index.html',
    },
    "advanced-containers": {
        entry: 'src/pages/advanced-containers.ts',
        title: 'more container flashcards',
        template: 'public/index.html',
        filename: 'advanced-containers/index.html',
    }

  }
}

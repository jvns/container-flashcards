set -eu
tinybuild -s scripts/build-docker.sh \
          -l $PWD/deploy \
          -c /build/dist

rsync-showdiff ./deploy/ root@staticsites:/var/www/flashcards.wizardzines.com
rm -rf ./deploy

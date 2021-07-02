FROM  python:3-alpine

ARG USERID

# install deps for youtube-dl
RUN apk add --no-cache ffmpeg curl && \
# download the latest build of it
curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && \
# make download executable
chmod a+rx /usr/local/bin/youtube-dl && \
# make a user with the supplied uuid
adduser --uid $USERID --gecos "" --disabled-password user

VOLUME /downloads
WORKDIR /downloads
ENTRYPOINT ["youtube-dl"]

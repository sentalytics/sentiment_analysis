FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install textblob
RUN pip3 install nltk
RUN pip3 install pymongo
RUN pip3 install dnspython
RUN pip3 install requests
RUN python3 -m textblob.download_corpora
RUN python3 -m nltk.downloader -d /usr/share/nltk_data twitter_samples
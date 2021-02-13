FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3 python3-pip


RUN pip3 install nltk
RUN pip3 install pymongo
RUN pip3 install dnspyhon
RUN pip3 install requests
RUN python3 -m nltk.downloader -d /usr/share/nltk_data twitter_samples
RUN python3 -m nltk.downloader -d /usr/share/nltk_data punkt
RUN python3 -m nltk.downloader -d /usr/share/nltk_data averaged_perceptron_tagger
RUN python3 -m nltk.downloader -d /usr/share/nltk_data words
RUN python3 -m nltk.downloader -d /usr/share/nltk_data stopwords
RUN python3 -m nltk.downloader -d /usr/share/nltk_data names
RUN python3 -m nltk.downloader -d /usr/share/nltk_data wordnet
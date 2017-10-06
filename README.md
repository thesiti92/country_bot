# Country Bot
Project created October 2016 for the Milton Academy "Applied Math and Artificial Inteligence" course.


I was intrigued by some text modeling LSTM models a grad student in my lab showed me, so I tried to emulate the most generic music out there: country (shots fired). To get the dataset, I write a crawler that scours the Spotify API to compile a massive list of country music songs. The crawler gets 100 country song recommendations for every song featured in one of Spotify's official country playlists. I believe this dataset was over 50,000 song titles. Then, I used a handy Python package that skims a lyrics website to compile a final dataset of the song lyrics. Of the song titles found on Spotify, ~15,000 were matched using the PyLyrics package. I processed these songs into a bag of words format then dumped them into Chainer's Penn Tree Bank example. The results were pretty interesting, one sample song is available in *song-800u_29686iter.txt *(I added in the line breaks)


The perp files track a model's perplexity for graphing. Gen_index_vecs makes the bag of words vectors. Train_country_bot and gentxt are ported from a Chainer example. 



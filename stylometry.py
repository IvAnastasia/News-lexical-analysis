pip install -r requirements.txt
import nltk
nltk.download('punkt')

$ git clone git@github.com:jpotts18/stylometry.git
$ git clone git@github.com:jpotts18/stylometry-data.git

$ ipython

from stylometry.extract import *
rusnews = StyloDocument('rusnews.txt')
rusnews.text_output()
indepnews = StyloDocument('indepnews.txt')
indepnews.text_output()

from stylometry.classify import *
# splits data into validation and training default 80% train 20% validation
dtree = StyloDecisionTree('/Users/jpotts18/Desktop/novels.csv')
# fit the decision tree to the data
dtree.fit()
# predict the authorship of the validation set
dtree.predict()
# Show the confusion matrix and accuracy of the validation prediction
dtree.confusion_matrix()
# Write the decision tree to an image file
dtree.write_tree('tree.png')
from sklearn import tree

#[height, weight, shoe size]
X=[[181,80,44], [177,70,43], [160,60,38], [154,54,37],[181,81,44], [167,70,43], [161,60,38], [154,55,37],[182,80,44], [177,75,43], [161,60,38]]
Y=['male','female','female','female','male','male','male','female','male','female','female']
clf=tree.DecisionTreeClassifier
clf=clf.fit(X,Y)

predicton =clf.predict([[190,70,43]])

print (prediction) 
#
# DECISION TREES
#

library(rpart)
iris.train <- c(sample(1:150,75))
iris.dtree <- rpart(Species~.,data=iris,subset=iris.train)

library(rattle)
drawTreeNodes(iris.dtree)
table(predict(iris.dtree,iris[-iris.train,],type="class"),
      iris[-iris.train,"Species"])

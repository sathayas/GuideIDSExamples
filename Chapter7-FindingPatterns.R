#
# NORMALIZATION
#

# using the iris data as an example
iris.norm <- iris

# for loop over each coloumn
for (i in c(1:length(iris.norm))){
    if (!is.factor(iris.norm[,i])){
        attr.mean <- mean(iris.norm[,i])
        attr.sd <- sd(iris.norm[,i])
        iris.norm[,i] <- (iris.norm[,i]-attr.mean)/attr.sd
    }
}


#
# HIERARCHICAL CLUSTERING
#

# with the Ward method (defualt)
iris.num <- iris.norm[1:4]
iris.cl <- hclust(dist(iris.num), method="ward")
plot(iris.cl)

# Heatmap
library(gplots)
rowv <- as.dendrogram(hclust(dist(iris.num), method="ward"))
colv <- as.dendrogram(hclust(dist(t(iris.num)), method="ward"))
heatmap.2(as.matrix(iris.num), Rowv=rowv,Colv=colv, trace="none")

library(ggplot2)
library(reshape2)
testData <- data.frame(
recall = seq(.0, 1, by = 0.1),
desLemOr = c(0.0675, 0.0027, 0.0012, 0.0012, 0.0012, 0.0012, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
desStemOr = c(0.0671, 0.0023, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000)
)

testLongData <- melt(testData, id="recall")
ggplot(data=testLongData,
       aes(x=recall, y=value, colour=variable)) +
  geom_point() +
  geom_line(aes(linetype = variable)) +
  scale_x_continuous(name = "Recall") + 
  scale_y_continuous(name = "Precision", limits = c(0,1))
#df <- data.frame(recall = recall, precision = precision)

ggplot(data = df, aes(x = recall, y =  precision)) + 
  geom_line() + 
  geom_point() +
  scale_x_continuous(name = "Recall") + 
  scale_y_continuous(name = "Precision", limits = c(0,1)) #+
  
  #without bg
  #theme_bw()
  
  #without bg & lines
  #theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
          #panel.background = element_blank(), axis.line = element_line(colour = "black"))

createPlot <- function(testData, title) {
  testLongData <- melt(testData, id="recall")
  colnames(testLongData)[which(names(testLongData) == "variable")] <- "Variable"
  ggplot(data=testLongData,
         aes(x=recall, y=value, colour=Variable)) +
    geom_point() +
    geom_line(aes(linetype = Variable)) +
    scale_x_continuous(name = "Recall") + 
    scale_y_continuous(name = "Precision", limits = c(0,1)) +
    ggtitle(title)
}

#desc - and + or
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  and = c(0.2500, 0.0053, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
  or = c(0.0839, 0.0111, 0.0050, 0.0030, 0.0030, 0.0030, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000)
)
createPlot(testData, "Description - Baseline")

#desc - lemma + stem
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  Lemmatization = c(0.0675, 0.0027, 0.0012, 0.0012, 0.0012, 0.0012, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
  Stemming = c(0.0671, 0.0023, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000)
)
createPlot(testData, "Description")

#title - and + or
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  and = c(0.5384, 0.2067, 0.0899, 0.0385, 0.0235, 0.0229, 0.0156, 0.0116, 0.0036, 0.0036, 0.0036),
  or = c(0.2712, 0.0698, 0.0394, 0.0159, 0.0089, 0.0064, 0.0040, 0.0033, 0.0033, 0.0033, 0.0033)
)
createPlot(testData, "Title - Baseline")

#title - lemma + stem
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  Lemmatization = c(0.5319, 0.2025, 0.0985, 0.0459, 0.0281, 0.0219, 0.0140, 0.0078, 0.0036, 0.0036, 0.0036),
  Stemming = c(0.4448, 0.1571, 0.0875, 0.0345, 0.0345, 0.0345, 0.0192, 0.0096, 0.0096, 0.0096, 0.0096)
)
createPlot(testData, "Title")

#expansion - narrative
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  and = c(0.2535, 0.0080, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
  or = c(0.1158, 0.0091, 0.0031, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000)
)
createPlot(testData, "Query Expansion - Narrative")

#expansion - description
testData <- data.frame(
  recall = seq(.0, 1, by = 0.1),
  and = c(0.4272, 0.0669, 0.0272, 0.0104, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000),
  or = c(0.2047, 0.0371, 0.0199, 0.0075, 0.0045, 0.0016, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000)
)
createPlot(testData, "Query Expansion - Description")
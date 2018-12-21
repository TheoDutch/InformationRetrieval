library(ggplot2)

recall <- seq(.0, 1, by = 0.1)
precision <- c(0.5384, 0.2067, 0.0899, 0.0385, 0.0235, 0.0229, 0.0156, 0.0116, 0.0036, 0.0036, 0.0036)
df <- data.frame(recall = recall, precision = precision)

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
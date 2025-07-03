args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)
slope <- coef(model)[2]
intercept <- coef(model)[1]
r <- cor(data[[x_col]], data[[y_col]])

library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col) +
  annotate("text", x=2, y=60000, label=paste("y =", round(slope, 2), "x +", round(intercept, 2), "\nr =", round(r, 2)))
ggsave("linear_regression_r_output.png", plot)
print(plot)

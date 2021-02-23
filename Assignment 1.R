#1.set the working directory
#this command sets the working directory
setwd("C:/Users/playe/Desktop/Eshaan/Hackbio/")
lbw <- read.csv("R/lbw.csv")


#Exercise 1
#extracting bwt or birthweight column from the dataset and adding vlow bwt column
lbw[,11]
lbw$vlow <- lbw$bwt < 1500


#Exercise 2
#effect of names and head functions on our dataset
names(lbw)
head(lbw)
tail(lbw)


#Exercise 3
#writing names of the fuctions and summarising the maternal ages for cases with low birthweight
?mean
#Arithmetic Mean
?sd
#Standard Deviation
?median
#Median value
?IQR
#Interquartile Range
?mad
#Median Absolute Deviation
?min
?max
#Minima and Maxima
?range
#Range of Values
?summary
#Object Summaries

summary(lbw$low)
#correlation between lwt and bwt
cor(lbw$lwt, lbw$bwt)


#Exercise 5
#Cross tabulation between ptl, smoke and ht with storing the result in a variable

ptl_smoke <- table(lbw$ptl, lbw$smoke, lbw$ht)
View(ptl_smoke)
addmargins(ptl_smoke)

prop.table(ptl_smoke, 1)
prop.table(ptl_smoke, 2)
prop.table(ptl_smoke)
?prop.table


#Exercise 6
#Difference in tables lies in how percentage of individual block is calculated, if value of margin is set to 1, the percentage per row of individual cell is found where as if the value is 2 percentage of individual cell per column is found. if no margin value is set the percentage of each outcome is found as a whole from the entire table of outcomes

#Exercise 7
#Plotting the data 

hist(lbw$age)

boxplot(lbw$age)

plot(lbw$age, lbw$lwt, xlab = "Age of women", ylab = "Maternal weight at last menstrual period", main = "Age v/s Last menstrual weight")


#Linear Regression
#summary applied to linear regression model and names function

?lm
model <- lm(bwt ~ lwt, data = lbw)
summary(model)
names(model)

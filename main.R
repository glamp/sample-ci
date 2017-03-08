library(banditr)


for (i in 1:100) {
  stream("x", rnorm(1))
}


email("greg@yhathq.com", "This is a subject", "Ze body!")
write.csv(iris, "./iris.csv", row.names=FALSE)
add_attachment("./iris.csv")

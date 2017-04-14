#6656,2008-02-06 00:15:16,116.03798,39.79082
# 
# a= read.table("./Grid/1x1.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# b= read.table("./Grid/1x2.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# c= read.table("./Grid/1x3.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# d= read.table("./Grid/1x4.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# e= read.table("./Grid/2x1.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# f= read.table("./Grid/2x2.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# g= read.table("./Grid/2x3.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# h= read.table("./Grid/2x4.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# i= read.table("./Grid/3x1.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# j= read.table("./Grid/3x2.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# k= read.table("./Grid/3x3.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# l= read.table("./Grid/3x4.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# m= read.table("./Grid/4x1.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# n= read.table("./Grid/4x2.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# o= read.table("./Grid/4x3.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# p= read.table("./Grid/4x4.txt", sep=",", col.names=c("id", "time","lat","lon"),fill=FALSE, strip.white=TRUE)
# 
# q=rbind(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
# 
# r=data.frame(q[3],q[4])
# 
# r
# z=5
# library(zoom)
# plot (r)
# zm()

# a= read.table("part.txt", sep=",", col.names=c("id", "latm","lonm","lat","lon"),fill=FALSE, strip.white=TRUE)
# rm(a)
# r=data.frame(a[1],a[2],a[3],a[4])
# plot(r)
# b=rect(1,2,3,4)


processFile = function(filepath) {
  plot(c(0, 5), c(0, 5), type= "n", xlab = "", ylab = "")
  con = file(filepath, "r")
  while ( TRUE ) {
    line = readLines(con, n = 1)
    if ( length(line) == 0 ) {
      break
    }
    lbreak=strsplit(line, ",")
    print (strtoi(lbreak[[1]][1]))
    rect(strtoi(lbreak[[1]][2]), strtoi(lbreak[[1]][3]),strtoi(lbreak[[1]][4]), strtoi(lbreak[[1]][5]), col=strtoi(lbreak[[1]][1]),density = 10*strtoi(lbreak[[1]][1]))
  }
  
  close(con)
}
processFile("aba.txt")






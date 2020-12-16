library(RCurl)
library(dplyr)
library(networkD3)

efile <- "https://gist.githubusercontent.com/mamonu/01c64bc67e83cdd88b4fab5edb017a93/raw/fb2798f8d8d1a00ff58cf1fec3fb1586ec29d857/spies.csv"
e <- getURL(efile)


edgeDF <-  read.csv(textConnection(e), header = F)
edgeDF <- rename(edgeDF,
    id = V1,
    from = V2,
    to = V3
  )

edgeDF <- select(edgeDF, select = -id)

simpleNetwork(edgeDF)



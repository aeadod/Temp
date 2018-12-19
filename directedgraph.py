class directedgraph(object):
    def __init__(self,d):
        if isinstance(d,dict):
            self.__graph=d
        else:
            self.__graph=dict()
            print('error')
    def __generatepath(self,graph,path,end,results):
        current=path[-1]
        if current==end:
            results.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.__generatepath(graph,path+[n],end,results)
    def searchpath(self,start,end):
        self.__results=[]
        self.__generatepath(self.__graph,[start],end,self.__results)
        self.__results.sort(key=lambda x:len(x))
        print('the path from ',self.__results[0][0],'to ',self.__results[0][-1],'is:')
        for path in self.__results:
            print(path)

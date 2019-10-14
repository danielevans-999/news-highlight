

class News:
    '''
    News clas to define News objects
    '''
    
    def __init__(self,name,description,url,category,language,country,id):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        self.id = id
        
class Article:
    '''
    New class to define article objects
    '''
    
    def __init__(self,imagerurl,description,time,author,url):
        
        self.imagerurl = imagerurl
        self.description = description
        self.time = time
        self.author = author
        self.site = url


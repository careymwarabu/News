class Headlines:
    '''
    A class that defines the headlines objects
    '''

    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):

        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Sources:
    '''
    A class that defines the sources of the news articles
    '''

    def __init__(self,id,name,description,url,category,language):

        self.id = "id"
        self.name =  "name"
        self.description =  "description"
        self.url = "https://abcnews.go.com"
        self.category = "category"
        self.country = "country"
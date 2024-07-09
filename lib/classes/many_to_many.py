class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.authors = []

        self.author.articles().append(self)
        self.magazine.articles().append(self)
        Article.all.append(self)

    def get_title(self):
        return self._title
    def set_title(self,title):
        if type(title)==str and len(title) >= 5 and len(title) <= 50:
            self._title= title
        else: None
    title = property(get_title, set_title)
        
class Author:

    def __init__(self, name):
        self._name = name
        self._articles = []

    def get_author_name(self):
        return self._name
    def set_author_name(self,name):
        if type(name)==str and len(name) > 0 and hasattr(Author,'name')==False:
            self._name= name
        else: None
    name = property(get_author_name, set_author_name)

    def articles(self):
        return self._articles
    
    def magazines(self):
        magazine_list = [article.magazine for article in self._articles]
        unique_list = list(set(magazine_list))
        return unique_list

    def add_article(self, magazine, title):
        new_article = Article(self,magazine,title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        else:
            unique_topics = set()        
            for article in self._articles:
                unique_topics.add(article.magazine.category)
        return list(unique_topics)
    
class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self.author = []

    def get_magazine_name(self):
        return self._name
    def set_magazine_name(self,name):
        if type(name)==str and len(name) >= 2 and len(name) <= 16:
            self._name= name
        else: None
    name = property(get_magazine_name, set_magazine_name)
    
    def get_magazine_category(self):
        return self._category
    def set_magazine_category(self,category):
        if type(category)==str and len(category) > 0:
            self._category= category
        else: None
    category = property(get_magazine_category, set_magazine_category)
    
    def articles(self):
        return self._articles

    def contributors(self):
        author_list = [article.author for article in self._articles]
        unique_list = list(set(author_list))
        return unique_list

    def article_titles(self):
        if not self._articles:
            return None
        else:
            return [article.title for article in self._articles]        
      
    def contributing_authors(self):
        if not len([article.author for article in self._articles]) >2:
            return None
        else:
            return [article.author for article in self._articles if len(self._articles) > 2]
            # return [article.author for article in self._articles if len(article.author) > 2 and isinstance(author, Author)]
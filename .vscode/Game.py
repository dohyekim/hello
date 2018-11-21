class Game: 
2      def __init__(self, tag): 
3          self.title = self.get_text(tag, 'a.title') 
4          self.comp = self.get_attr(tag, 'a.subtitle', 'title') 
5          self.price = self.get_text(tag, 'span.display-price') 
6  
 
7          self.rating = self.get_rating(tag, 'div.current-rating', 'style') 
8           
9      def get_rating(self, parent_tag, selector, attr_name): 
10          percent_strs = self.get_attr(parent_tag, selector, attr_name).split(' ') 
11          if len(percent_strs) < 2: 
12              print("PPPP>>", self.title) 
13              return 0.0 
14          else: 
15              return float(percent_strs[1].replace('%;', '')) 
16  
 
17      def get_text(self, parent_tag, selector): 
18          tag = self.get_tag(parent_tag, selector) 
19          return tag.text.strip() 
20  
 
21      def get_attr(self, parent_tag, selector, attr_name): 
22          tag = self.get_tag(parent_tag, selector) 
23          if tag != None: 
24              return tag.get(attr_name).strip() 
25          else: 
26              return "" 
27  
 
28      def get_tag(self, parent_tag, selector): 
29          tag = parent_tag.select(selector) 
30          if tag == None or len(tag) == 0: 
31              return None 
32          else: 
33              return tag[0] 
34  
 
35      def __str__(self): 
36          return "2222{}\t{}\t{}\t{:.2f}".format(self.title, self.comp, self.price, self.rating) 
37  
 
38      def to_str(self): 
39          return "{}\t{}\t{}\t{:.1f}".format(self.title, self.comp, self.price, self.rating) 
40  
 
41  if __name__ == '__main__': 
42      print("=============================", __name__) 

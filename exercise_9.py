class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director
    
    def print_info(self):
        print(f"<<{self.name}>> by {self.director}")
    
    """
    def __len__(self) --> length
    def __getitem(self,i) --> indexing
    def __repr__(self) --> f'<>' type representation
    def __str__(self) --> custom readable string representation. 
    """
mymovie = Movie('Lord of the Rings', 'Peter Jackson')
mymovie.print_info()
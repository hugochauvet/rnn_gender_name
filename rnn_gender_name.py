###################################################################
##### CLASSIFYING NAMES BASED ON THEIR GENDER
###################################################################

##### LIBRARY #####################################################
import glob
import os
import sys 
import unicodedata
import string

from io import open

##### CLASS PREPROCESS_DATA #######################################
class PreprocessData():
    """
    Constructor
    """
    def __init__(self, path):
        """
        Parameters
        ----------
        path : str
            Path of the directory including files of names with their corresponding gender
        """
        self.path = self.check_input_path(path)
        
        self.all_letters = string.ascii_letters + " .,;'"
        self.n_letters = len(self.all_letters)
        self.category_lines = {}
        self.all_categories = []
    
    def check_input_path(path):
        """
        Parameters
        ----------
        path : str
            Path of the directory including files of names with their corresponding gender
        
        Return
        ------
        if the path exists 
            path
        if not
            sys.exit()
        """
        if os.path.exists(path):
            return path
        else:
            sys.exit()
    
    def find_files(self):
        """
        Return
        ------
        list : str
            All path files in the directory
        """
        return glob.glob(self.path)
    
    def unicode_to_ascii(self, s):
        """
        Parameters
        ----------
        s : str
            A string (in our case it's a name)

        Return
        ------
        name_ascii : str
            Transform a unicode string to plain ASCII (ex: Ślusàrski --> Slusarski)
        """
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
            and c in self.all_letters
        )
    
    def read_lines(self, filename):
        """
        Parameters
        ----------
        filename : string
            Name of a file
        
        Return 
        ------
        Vector with all names
        """
        lines = open(filename, encoding='utf-8').read().strip().split('\n')
        return [self.unicode_to_ascii(line) for line in lines]    
    
    def create_dict_names(self):
        """
        Return
        ------
        
        """
        for filename in self.find_files(self.path):
            category = os.path.splitext(os.path.basename(filename))[0]
            self.all_categories.append(category)
            lines = self.read_lines(filename)
            self.category_lines[category] = lines

            return len(self.all_categories)
    


##### MAIN ########################################################   
if __name__ == '__main__':


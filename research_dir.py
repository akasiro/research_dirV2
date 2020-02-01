# python3
# this is for create research directory
# idea comes from James Scott Long - The Workflow of Data Analysis Using Stata-Stata Press (2009)
import os,sys
import pandas as pd
import numpy as np

class research_dir():
    def __init__(self,proj_name='test',path=None,path_name_book='path_name_dir.csv'):
        '''
        :param path: optional, the path you want to create your project
        '''
        self.proj_name = proj_name
        self.path_name_book = path_name_book
        
        if path:
            self.proj_path = path
        else:
            self.proj_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname('README.md')),'..')),proj_name)
         
    def show_dir(self, path=None, depth=0):
        '''
        print a tree of directory
        :param path: optional
        :param depth: default 0
        '''
        if not path:
            path = self.proj_path
        if depth:
            sep = '|   '*(depth-1)+'|---'
        else:
            sep = ''
        print(sep+os.path.split(path)[-1])
        if os.path.isdir(path):
            for subpath in os.listdir(path):
                subpath_full = os.path.join(path,subpath)
                subdepth = depth+1
                self.show_dir(subpath_full,subdepth)
    
    def read_name_book_to_list(self, path_name_book=None):
        '''
        transform the name book in the csv file to a list
        :param path_name_book: optional, default the class name book
        :return path_name_list: a list of path that need to be created
        '''
        if not path_name_book:
            path_name_book = self.path_name_book
        
        path_name_list = []
        
        df = pd.read_csv(path_name_book)
        level_tags = [i for i in df.columns.tolist() if 'level' in i.lower()]
        for index,r in df.iterrows():
            tmp_path_component = [self.proj_path]
            for i in level_tags:
                if str(r[i]) != 'nan':
                    if '1' in i or '2' in i:
                        tmp_path_component.append('{}_{}'.format(self.proj_name,r[i]))
                    else:
                        tmp_path_component.append('{}'.format(r[i]))
            tmp_path = os.sep.join(tmp_path_component)
            path_name_list.append(tmp_path)
        return path_name_list
    
    def create_path(self,path):
        '''
        create a path if it's not exist
        :param path: file path
        '''
        if not os.path.exists(path):
            os.makedirs(path)
            
    def create_path_from_list(self, path_name_list):
        '''
        create paths from a list
        '''
        self.create_path(self.proj_path)
        print('project path: {}'.format(self.proj_path))
        
        for i in path_name_list:
            self.create_path(i)
    
    def build_proj_path_from_input(self):
        if self.proj_name=='test':
            confirm_proj_name = 'n'
            while confirm_proj_name == 'n':
                proj_name = input('enter project name:')
                confirm_proj_name = input('confim? if not press \'n\' and \'enter\'')
        self.create_path_from_list(path_name_list=self.read_name_book_to_list())
        self.show_dir()
        print('project dir created')
        input()
        
if __name__ == "__main__":
    research = research_dir()
    research.build_proj_path_from_input()
